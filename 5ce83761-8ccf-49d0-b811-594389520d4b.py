#!/usr/bin/env python
# coding: utf-8

# <div style="border:solid Chocolate 2px; padding: 40px">
# 
# <b>Сергей, привет!</b>
# 
# Меня зовут Евгений Головин, я буду ревьюером твоего проекта. Если ты не против, то предлагаю построить наше общение на "ты" ;) Если удобнее на "вы", то нет проблем, только скажи об этом. 
# 
# В ходе работы я оставил тебе комментарии <font color='green'>зеленого</font>, <font color='gold'>желтого</font> и <font color='red'>красного</font> цветов. Сейчас объясню, что они значат:
# 
# <br/>
# 
# <div class="alert alert-success">
# <h2> Комментарий ревьюера <a class="tocSkip"> </h2>
# 
# <b>Все супер!👍:</b> Решение на этом шаге является полностью правильным.
# </div>
# 
# <br/>
# 
# <div class="alert alert-warning">
#     <h2> Комментарий ревьюера <a class="tocSkip"> </h2>
#     
# <b>Небольшие замечания и рекомендации💡:</b> Решение на этом шаге станет еще лучше, если внести небольшие коррективы.
# </div>
# 
# 
# <br/>
# <div class="alert alert-block alert-danger">
# <h2> Комментарий ревьюера <a class="tocSkip"></h2>
# 
#     
# <b>На доработку🤔:</b>
#  Решение на этом шаге требует существенной переработки и внесения правок. Напоминаю, что проект не может быть принят с первого раза, если ревью содержит комментарии, рекомендующие доработать шаги.
# </div>
#     
# Увидев мой комментарий, не удаляй его, он будет очень полезен в случае повторной проверки работы :)
#     
# <div class="alert alert-info">
# <b> На мои комменатрии можно и нужно реагировать, только делать это стоит так, чтобы твои и мои комменты не смешались: выделяй свои цветами, сильно отличающимися от моих, например вот так, синим фоном</b> 
# </div>
#     
#     
# Увидев у тебя неточность, в первый раз я лишь укажу на ее наличие и дам тебе возможность найти и исправить ее. На реальной работе твой руководитель будет поступать также, и я пытаюсь подготовить тебя именно к работе аналитиком. Но если ты пока не справишься с такой задачей - при следующей проверке я дам более точную подсказку!

# ## Исследование данных о российском кинопрокате
# 
# 

# <div class="alert alert-warning">
#     <h2> Комментарий ревьюера v1<a class="tocSkip"> </h2>
#     
# <b>Небольшие замечания и рекомендации💡:</b> Введение напишем?

# ### Шаг 1. Откройте файлы с данными и объедините их в один датафрейм. 
# 
# Объедините данные таким образом, чтобы все объекты из датасета `mkrf_movies` обязательно вошли в получившийся датафрейм. 
# 
# <div id="accordion">
#     <div class="card">
#         <div class="card-header" id="headingThree">
#             <button class="btn btn-link collapsed" data-toggle="collapse" data-target="#collapseHint_0" aria-expanded="false" aria-controls="collapseHint_0">Подсказка</button>
#         </div>
#         <div id="collapseHint_0" class="collapse" aria-labelledby="headingThree" data-parent="#accordion">
#             <div class="card-body">
# Обратите внимание на тип данных столбца, по которому будете соединять датафреймы. Тип данных этих столбцов должен быть одинаковым в обоих датафреймах.
#             </div>
#         </div>
#     </div>
# </div>

# In[56]:


import pandas as pd
df_1 = pd.read_csv('/datasets/mkrf_movies.csv')
df_2 = pd.read_csv('/datasets/mkrf_shows.csv')
df_1.info()
df_2.info()




# In[ ]:





# Читаем таблицы данных и смотрим общую информацию

# In[57]:


df_1.loc[1797, 'puNumber'] = '0' # Так как программа выдавала ошибку что в строке 1797, слово нет, проводим замену на ноль
df_1['puNumber'] = pd.to_numeric(df_1['puNumber'])
df_1['puNumber'].dtype


# In[58]:


df = df_1.merge(df_2, how='left')
df.head(10)


# Приводим столбцы, объединяющие обе таблицы данных, к одинаковому типу и объединяем  таблицы

# <div class="alert alert-success">
# <h2> Комментарий ревьюера v1<a class="tocSkip"> </h2>
# 
# <b>Все супер!👍:</b> Все по делу, да) Подскажу только, что если у to_numeric() правильно настроить значение errors, то вручную удалять аномалии будет не нужно

# ### Шаг 2. Предобработка данных

# #### Шаг 2.1. Проверьте типы данных
# 
# - Проверьте типы данных в датафрейме и преобразуйте их там, где это необходимо.

# In[59]:


df.info()


# In[60]:


df['show_start_date'] = pd.to_datetime(df['show_start_date'], format = '%Y/%m/%d')


# <div class="alert alert-success">
# <h2> Комментарий ревьюера v1<a class="tocSkip"> </h2>
# 
# <b>Все супер!👍:</b> Дата должна ыбть датой, да

# Переводим столбец времени премьеры киноленты в формат даты без времени.

# In[61]:


df['ratings'].unique()


# In[62]:


df['ratings'] = pd.to_numeric(df['ratings'], errors='coerce', downcast='float')
df['ratings'].unique()


# <div class="alert alert-success">
# <h2> Комментарий ревьюера v1<a class="tocSkip"> </h2>
# 
# <b>Все супер!👍:</b> Сам все умеешь)

# Приводим тип данных столбца ratings к float

# #### Шаг 2.2. Изучите пропуски в датафрейме
# 
# - Объясните, почему заполнили пропуски определённым образом или почему не стали этого делать.

# In[63]:


df.isna().sum()


# Большинство пропусков связано с поддержкой и бюджетом, я думаю это связано с тем, что многие фильмы просто неполучили поддержки, поэтому же неизвестен источник поддержки. Это не объясняет отсутствия значений по бюджету, но по видимому в нашем датафреймы бюджеты известны только у картин с поддержкой.
# Также есть отстуствие данных по сборам, так как мы добавили только 3158 строк данных по сборам, остальные нам неизвестны. Все остальные пропуски связаны как мне кажется просто с не заполнением. Вся информация должна быть в открытом поиске, но восстановление данных займет уйму времени.

# <div class="alert alert-success">
# <h2> Комментарий ревьюера v1<a class="tocSkip"> </h2>
# 
# <b>В
#     се супер!👍:</b> Так и есть, молодец!
#     

# #### Шаг 2.3. Изучите дубликаты в датафрейме
# - Проверьте, есть ли в данных дубликаты. Опишите причины, которые могли повлиять на появление дублей.

# In[64]:


print('Количество дублирующихся строк:' ,df.duplicated().sum())
df.nunique()


# In[65]:


df.loc[df['title'].duplicated(keep=False)].sort_values(by='title')


# <div class="alert alert-info"> <b></b> Повторы в title имеют разные даты премьеры и прокатные удостоверения. Вероятно один и тоже фильм показывают разные прокатчики, в разное время отсюда и повторы 

# In[66]:


df.loc[df['puNumber'].duplicated(keep=False)]


# <div class="alert alert-info"> <b></b> puNumber должен быть уникальным , поэтому дубликаты в этом столбце вероятно являются человеческой ошибкой при заполнении

# <div class="alert alert-block alert-danger">
# <h2> Комментарий ревьюера v1<a class="tocSkip"></h2>
# 
# <b>На доработку🤔:</b>  Явных нет, но можно и нужно поискать неявные, например по номеру проектного удостоверения и названию фильма

# <div class="alert alert-success">
# <h2> Комментарий ревьюера v2 <a class="tocSkip"> </h2>
# 
# <b>Все супер!👍:</b> Отлично!

# #### Шаг 2.4. Изучите категориальные значения
# 
# - Посмотрите, какая общая проблема встречается почти во всех категориальных столбцах;
# - Исправьте проблемные значения в поле `type`.
# 
# <div id="accordion">
#     <div class="card">
#         <div class="card-header" id="headingThree">
#             <button class="btn btn-link collapsed" data-toggle="collapse" data-target="#collapseHint_1" aria-expanded="false" aria-controls="collapseHint_1">Подсказка</button>
#         </div>
#         <div id="collapseHint_1" class="collapse" aria-labelledby="headingThree" data-parent="#accordion">
#             <div class="card-body">
# В поле <code>type</code> есть несколько значений, у которых появился пробел в начале строки. Самый простой способ их «починить» -- использовать метод <a href="https://pandas.pydata.org/docs/reference/api/pandas.Series.str.strip.html#pandas.Series.str.strip">.str.strip</a>. Этот метод удаляет все пробелы, которые встречаются в начале и в конце строки. Применяют его таким образом:<br>
# <code>df['type'].str.strip()</code>
#             </div>
#         </div>
#     </div>
# </div>

# In[67]:


df['type'].unique()


# In[68]:


df['type'] = df['type'].str.strip()
df['type'].unique()


# <div class="alert alert-success">
# <h2> Комментарий ревьюера v1<a class="tocSkip"> </h2>
# 
# <b>Все супер!👍:</b> Это важно

# Избавились от лишних пробелов

# In[69]:


df['age_restriction'].unique()


# в столбце age_restriction все в норме

# In[70]:


df['genres'] = df['genres'].str.strip()
df['genres'].unique()


# In[71]:


df['financing_source'].unique()


# In[72]:


df['production_country'] = df['production_country'].str.strip()
df['production_country'].unique()


#  <div class="alert alert-block alert-danger">
# <h2> Комментарий ревьюера v1<a class="tocSkip"></h2>
# 
# <b>На доработку🤔:</b>  Что можешь сказать по поводу жанров? По поводу стобла со страной произсводства?

# <div class="alert alert-info"> <b></b> В genres и production_country очень много различных комбинаций, отсюда не так много повторений. 

# <div class="alert alert-success">
# <h2> Комментарий ревьюера v2 <a class="tocSkip"> </h2>
# 
# <b>Все супер!👍:</b> Верно)

# #### Шаг 2.5. Проверьте количественные значения
# 
# - Проверьте, обнаружились ли в таких столбцах подозрительные данные. Как с такими данными лучше поступить?
# 
# <div id="accordion">
#     <div class="card">
#         <div class="card-header" id="headingThree">
#             <button class="btn btn-link collapsed" data-toggle="collapse" data-target="#collapseHint_budget" aria-expanded="false" aria-controls="collapseHint_budget">Подсказка</button>
#         </div>
#         <div id="collapseHint_budget" class="collapse" aria-labelledby="headingThree" data-parent="#accordion">
#             <div class="card-body">
# Обратите внимание на описание столбца <code>budget</code>. Как этот столбец соотносится с двумя другими: <code>refundable_support</code> и <code>nonrefundable_support</code>?
#             </div>
#         </div>
#     </div>
# </div>

# In[73]:


supported = df[df['nonrefundable_support'] > 0]
supported.head(20)


# Есть строки где на фильм была выделена поддержка, но бюджет равен нулю, надо проверить сколько их.

# In[74]:


wrong_budget = df[df['budget'] < df['refundable_support'] + df['nonrefundable_support']]
wrong_budget


# Попытаемся заполнить данные о бюджете высчитав медианный процент поддержки от общего бюджета

# In[75]:


df['percentage'] = (df['refundable_support'] + df['nonrefundable_support'] / df['budget'])
percentage = df['percentage'].median()
percentage


# In[76]:


df.loc[wrong_budget.index, 'budget'] = (df.loc[wrong_budget.index, 'refundable_support'] + df.loc[wrong_budget.index, 'nonrefundable_support']) / percentage

df.loc[wrong_budget.index]


# <div class="alert alert-success">
# <h2> Комментарий ревьюера v1<a class="tocSkip"> </h2>
# 
# <b>Все супер!👍:</b> Идеально!

# #### Шаг 2.6. Добавьте новые столбцы
# 
# 
# 
# 

# - Создайте столбец с информацией о годе проката. Выделите год из даты премьеры фильма.

# In[77]:


df['year'] = df['show_start_date'].dt.year
df.head()


# - Создайте два столбца: с именем и фамилией главного режиссёра и основным жанром фильма. В столбцы войдут первые значения из списка режиссёров и жанров соответственно.
# 
# <div id="accordion">
#     <div class="card">
#         <div class="card-header" id="headingThree">
#             <button class="btn btn-link collapsed" data-toggle="collapse" data-target="#collapseHint_2" aria-expanded="false" aria-controls="collapseHint_2">Подсказка</button>
#         </div>
#         <div id="collapseHint_2" class="collapse" aria-labelledby="headingThree" data-parent="#accordion">
#             <div class="card-body">
# Чтобы создать такие столбцы, лучше всего использовать собственную функцию. Эту функцию можно применить к двум столбцам сразу. 
#             </div>
#         </div>
#     </div>
# </div>

# In[78]:


def first(df, columns):
    for column in columns:
        df[f'main_{column}'] = df[column].dropna().apply(lambda x: x.split(',')[0])
    return df


# In[79]:


df = first(df, ['director', 'genres'])
df.head(20)


# - Посчитайте, какую долю от общего бюджета фильма составляет государственная поддержка.

# In[80]:


percentage


# <div class="alert alert-success">
# <h2> Комментарий ревьюера v1<a class="tocSkip"> </h2>
# 
# <b>Все супер!👍:</b> Все столбцы добавлены верно!

# ### Шаг 3. Проведите исследовательский анализ данных
# 

# - Посмотрите, сколько фильмов выходило в прокат каждый год. Обратите внимание, что данные о прокате в кинотеатрах известны не для всех фильмов. Посчитайте, какую долю составляют фильмы с указанной информацией о прокате в кинотеатрах.

# In[81]:


df_pivot = df.loc[df['box_office'].notna(), ['year', 'box_office']]                  .groupby('year')                 .agg(['count', 'sum', 'mean', 'median']) 
                

df_pivot.columns = df_pivot.columns.get_level_values(1) 
df_pivot.columns
df_pivot


# In[82]:


df.loc[df['box_office'].notna()].pivot_table(index='year',values='title',aggfunc='count').plot(kind = 'line')


# Если смотреть по фильмам с доступными сборами, то с  каждым годом видим увелечение выпущенных картин за исключением 17 года. 

# In[83]:


available_box_info = df['box_office'].notna().mean()
available_box_info


# Процент кинолент с доступной информацией по сборам

# <div class="alert alert-warning">
#     <h2> Комментарий ревьюера v1<a class="tocSkip"> </h2>
#     
# <b>Небольшие замечания и рекомендации💡:</b> Супер, но не хватает визуализаций по первому вопросу

# - Изучите, как менялась динамика проката по годам. В каком году сумма сборов была минимальной? А максимальной?

# In[84]:


df_pivot.plot(title='сборы фильмов', kind='line', y='sum')
print(f"В {df_pivot['sum'].idxmin()} году сумма сборов была минимальной, в {df_pivot['sum'].max()} максимальной.")


# <div class="alert alert-success">
# <h2> Комментарий ревьюера v1<a class="tocSkip"> </h2>
# 
# <b>Все супер!👍:</b> Хорошо!

# - С помощью сводной таблицы посчитайте среднюю и медианную сумму сборов для каждого года.

# In[85]:


df_pivot.plot(title='средняя и медианная сумма сборов по годам', kind='line', y=['median', 'mean'])


# <div class="alert alert-success">
# <h2> Комментарий ревьюера v1<a class="tocSkip"> </h2>
# 
# <b>Все супер!👍:</b> Отлично!

# - Определите, влияет ли возрастное ограничение аудитории («6+», «12+», «16+», «18+» и т. д.) на сборы фильма в прокате в период с 2015 по 2019 год? Фильмы с каким возрастным ограничением собрали больше всего денег в прокате? Меняется ли картина в зависимости от года? Если да, предположите, с чем это может быть связано.

# In[86]:


age_dependance = df[df['box_office'].notna()].pivot_table(index='year',columns='age_restriction',values='box_office',aggfunc='sum')
age_dependance.plot(title='сумма сборов по годам с разбивкой по возрастным категориям', kind='line', xlim=[2015, 2019],figsize=(20, 10))


# Как правило фильмы категории 16+ имеют более высокие сборы

# <div class="alert alert-success">
# <h2> Комментарий ревьюера v1<a class="tocSkip"> </h2>
# 
#     
# <b>Все супер!👍:</b> Отлично, молодец!

# ### Шаг 4. Исследуйте фильмы, которые получили государственную поддержку
# 
# На этом этапе нет конкретных инструкций и заданий — поищите интересные закономерности в данных. Посмотрите, сколько выделяют средств на поддержку кино. Проверьте, хорошо ли окупаются такие фильмы, какой у них рейтинг.

# In[87]:


df['support'] = df['refundable_support'] + df['nonrefundable_support']
df['profitability'] =(df['box_office'] / df['support']) 
df['profitable'] = (df['profitability'] > 1)
df_supported = df.loc[df['refundable_support'].notna() | df['nonrefundable_support'].notna()]
df_supported['profitable'].value_counts().plot( kind='bar')

df_supported




# Фильмов который отбили вложения в два раза меньше, чем убыльных

# In[88]:


df_supported['ratings'].value_counts().plot(title ='Рейтинги фильмов,получивших поддержку', kind='bar', figsize = (25,10))
df_supported['ratings'].max()

df_supported['ratings'].mean()


# Максимальный рейтинг 8,5 , но средний 6, что не очень высоко

# In[89]:


df_supported['main_genres'].value_counts().plot(title ='Жанры фильмов,получивших поддержку', kind='bar', figsize = (25,10))


# Самые популярные жанры из получивших поддержку, это Драма и Комедия

# In[90]:


df_supported.groupby('main_genres')             .agg('mean')             .sort_values(by='profitability',
                         ascending=False) \
            .plot(title='средняя рентабельность фильма (по жанрам)',
                  kind='bar',
                  stacked=True,
                  y='profitability',
                 figsize = (25,10))


# In[91]:


df_supported.nlargest(40,'profitability').groupby('main_director')             .agg('mean')             .sort_values(by='profitability',
                         ascending=False) \
            .plot(title='средняя рентабельность фильма (по режиссерам)',
                  kind='bar',
                  stacked=True,
                  y='profitability',
                 figsize = (15,20))


# 

# In[92]:


df_supported.nlargest(40,'profitability').groupby('film_studio')             .agg('mean')             .sort_values(by='profitability',
                         ascending=False) \
            .plot(title='средняя рентабельность фильма (по студиям)',
                  kind='bar',
                  stacked=True,
                  y='profitability',
                 figsize = (15,20))


# In[ ]:





# <div class="alert alert-info"> <b></b> Вроде как получилось
#     

# <div class="alert alert-block alert-danger">
# <h2> Комментарий ревьюера v1<a class="tocSkip"></h2>
# 
# <b>На доработку🤔:</b>  Давай еще поисследуем, например окупаемость фильмов, режиссеров, студии

# <div class="alert alert-block alert-danger">
# <h2> Комментарий ревьюера v2 <a class="tocSkip"></h2>
#    
# <b>На доработку🤔:</b> Много комбинаций, как ты и говорил. Попробуй визуализировать не все данные, а только топовые, топ-10 или топ-15

# <div class="alert alert-success">
# <h2> Комментарий ревьюера v3 <a class="tocSkip"> </h2>
# 
# <b>Все супер!👍:</b> Топ!

# ### Шаг 5. Напишите общий вывод

# 

#    <div class="alert alert-info"> <b></b>
#    В данном проекте мы работали с набором данных, который содержит информацию о прокатных удостоверениях, сборах и государственной поддержке фильмов, а также информацию с сайта КиноПоиск. Мы изучили типы данных, пропуски и дубликаты в данном массиве данных. Также изучили столбцы с категориальными и количественными данными на подозрительные данные и по возможности исправили их.
#     Мы работали с данными в которых присутствует информация о сборах. Создали новые столбцы для анализа. Изучали динамику выхода фильмов по годам, а также изучили сборы кинолент и их зависимость от возрастной категории. 
#     После этого мы начали анализ исключительно фильмов получивших гос. поддержку. И выявили рейтинги этих фильмов, процент оккупаемости и среднии рентабельности в зависимости от жанра, режиссера и киностудии

# <div class="alert alert-block alert-danger">
# <h2> Комментарий ревьюера v1<a class="tocSkip"></h2>
# 
# <b>На доработку🤔:</b> итоговый вывод должен отражать проделанную работу полностью, а наш сейчас не отражает

# <div class="alert alert-success">
# <h2> Комментарий ревьюера v2 <a class="tocSkip"> </h2>
# 
# <b>Все супер!👍:</b> Итоговый вывод полностью отражает проделанную работу

# <div style="border:solid Chocolate 2px; padding: 40px">
#     
# **Общий вывод по проекту ревьювера**:
#  Сергей, спасибо за  проект! Ты приложил много усилий, чтобы довести его до конца, проделана огромная работа, и это видно невооруженным глазом, ты большой молодец!
#     
# **Отмечу положительные моменты**:
#     
#     1. Все разложено по полочкам, всегда понятен ход твоих мыслей, приятно смотреть
#     
#     2. Отличные визуализации
#     
#     2. На разных шагах проекта ты предлагала очень интересные решения и методы для их реализации. Хорошая работа!
#     
#     
# **На что стоит обратить внимание**:
#     
#     1. Не проверены неявные дубли
# 
#     2. Отечественные фильмы почти не исследованы
# 
#     3. Итоговый вывод
#     
#     
# **Удачи и жду твой проект на повторное ревью!**

# <div style="border:solid Chocolate 2px; padding: 40px">
#     
# **Общий вывод по проекту ревьювера v2**:
#  Сергей, остался момент с графиками и проект будет зачтен

# <div style="border:solid Chocolate 2px; padding: 40px">
#     
# **Общий вывод по проекту ревьювера v3**:
#  Сергей, ошибки исправлены, проект принят, поздравляю тебя! Успешной учебы и еще увидимся в Практикуме!
