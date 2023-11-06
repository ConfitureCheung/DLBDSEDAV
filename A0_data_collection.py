import pandas as pd
import numpy as np
import os

# Step1) Consolidate All Columns Name
# To simplify the works after
path = "E:\\IU_courses\\HOMEWORK\\Dataset"


# read file #
yr = 2015
csv15 = pd.read_csv(f"{path}\\happiness\\{yr}.csv")
# print(len(csv15.columns) + 1, csv15.columns)

# rename col
csv15.rename(columns={'Happiness Rank': 'Rank', 'Happiness Score': 'Score', 'Standard Error': 'SE'}, inplace=True)

# add year
csv15['Year'] = yr

# reorder col
csv15 = csv15[['Year', 'Country', 'Region', 'Rank', 'Score', 'SE', 'Economy (GDP per Capita)', 'Family',
               'Health (Life Expectancy)', 'Freedom', 'Trust (Government Corruption)', 'Generosity', 'Dystopia Residual']]

print(len(csv15.columns), csv15.columns)  # 13


# read file #
yr = 2016
csv16 = pd.read_csv(f"{path}\\happiness\\{yr}.csv")
# print(len(csv16.columns) + 1, csv16.columns)

# rename col
csv16.rename(columns={'Happiness Rank': 'Rank', 'Happiness Score': 'Score', 'Lower Confidence Interval': 'CI Low',
                      'Upper Confidence Interval': 'CI High'}, inplace=True)

# add year
csv16['Year'] = yr

# reorder col
csv16 = csv16[['Year', 'Country', 'Region', 'Rank', 'Score', 'CI Low', 'CI High', 'Economy (GDP per Capita)', 'Family',
               'Health (Life Expectancy)', 'Freedom', 'Trust (Government Corruption)', 'Generosity', 'Dystopia Residual']]

print(len(csv16.columns), csv16.columns)  # 14


# read file #
yr = 2017
csv17 = pd.read_csv(f"{path}\\happiness\\{yr}.csv")
# print(len(csv17.columns) + 1, csv17.columns)

# rename col
csv17.rename(columns={'Happiness.Rank': 'Rank', 'Happiness.Score': 'Score', 'Whisker.high': 'Whisker High',
                      'Whisker.low': 'Whisker Low', 'Economy..GDP.per.Capita.': 'Economy (GDP per Capita)',
                      'Health..Life.Expectancy.': 'Health (Life Expectancy)',
                      'Trust..Government.Corruption.': 'Trust (Government Corruption)',
                      'Dystopia.Residual': 'Dystopia Residual'}, inplace=True)

# add year
csv17['Year'] = yr

# reorder col
csv17 = csv17[['Year', 'Country', 'Rank', 'Score', 'Whisker High', 'Whisker Low', 'Economy (GDP per Capita)', 'Family',
               'Health (Life Expectancy)', 'Freedom', 'Trust (Government Corruption)', 'Generosity', 'Dystopia Residual']]

print(len(csv17.columns), csv17.columns)  # 13


# read file #
yr = 2018
csv18 = pd.read_csv(f"{path}\\happiness\\{yr}.csv")
# print(len(csv18.columns) + 1, csv18.columns)

# rename col
csv18.rename(columns={'Country or region': 'Country', 'Overall rank': 'Rank',
                      'GDP per capita': 'Economy (GDP per Capita)', 'Social support': 'Family',
                      'Healthy life expectancy': 'Health (Life Expectancy)', 'Freedom to make life choices': 'Freedom',
                      'Perceptions of corruption': 'Trust (Government Corruption)'}, inplace=True)

# add year
csv18['Year'] = yr

# reorder col
csv18 = csv18[['Year', 'Country', 'Rank', 'Score', 'Economy (GDP per Capita)', 'Family', 'Health (Life Expectancy)',
               'Freedom', 'Trust (Government Corruption)', 'Generosity']]

print(len(csv18.columns), csv18.columns)  # 10


# read file #
yr = 2019
csv19 = pd.read_csv(f"{path}\\happiness\\{yr}.csv")
# print(len(csv19.columns) + 1, csv19.columns)

# rename col
csv19.rename(columns={'Country or region': 'Country', 'Overall rank': 'Rank',
                      'GDP per capita': 'Economy (GDP per Capita)', 'Social support': 'Family',
                      'Healthy life expectancy': 'Health (Life Expectancy)', 'Freedom to make life choices': 'Freedom',
                      'Perceptions of corruption': 'Trust (Government Corruption)'}, inplace=True)

# add year
csv19['Year'] = yr

# reorder col
csv19 = csv19[['Year', 'Country', 'Rank', 'Score', 'Economy (GDP per Capita)', 'Family', 'Health (Life Expectancy)',
               'Freedom', 'Trust (Government Corruption)', 'Generosity']]

print(len(csv19.columns), csv19.columns)  # 10


# read file #
yr = 2020
csv20 = pd.read_csv(f"{path}\\happiness\\{yr}.csv")
# print(len(csv20.columns) + 1, csv20.columns)

# remove col to avoid duplication
csv20.drop(['Generosity'], axis=1, inplace=True)

# rename col
csv20.rename(columns={'Country name': 'Country', 'Regional indicator': 'Region', 'Ladder score': 'Score',
                      'Standard error of ladder score': 'SE', 'upperwhisker': 'Whisker High', 'lowerwhisker': 'Whisker Low',
                      'Explained by: Log GDP per capita': 'Economy (GDP per Capita)',
                      'Explained by: Social support': 'Family',
                      'Explained by: Healthy life expectancy': 'Health (Life Expectancy)',
                      'Explained by: Freedom to make life choices': 'Freedom',
                      'Explained by: Perceptions of corruption': 'Trust (Government Corruption)',
                      'Explained by: Generosity': 'Generosity',
                      'Dystopia + residual': 'Dystopia Residual'}, inplace=True)

# add year
csv20['Year'] = yr

# reorder col
csv20 = csv20[['Year', 'Country', 'Region', 'Score', 'SE', 'Whisker High', 'Whisker Low', 'Economy (GDP per Capita)',
               'Family', 'Health (Life Expectancy)', 'Freedom', 'Trust (Government Corruption)', 'Generosity', 'Dystopia Residual']]

print(len(csv20.columns), csv20.columns)  # 14


# read file #
yr = 2021
csv21 = pd.read_csv(f"{path}\\happiness\\{yr}.csv")
# print(len(csv21.columns) + 1, csv21.columns)

# remove col to avoid duplication
csv21.drop(['Generosity'], axis=1, inplace=True)

# rename col
csv21.rename(columns={'Country name': 'Country', 'Regional indicator': 'Region', 'Ladder score': 'Score',
                      'Standard error of ladder score': 'SE', 'upperwhisker': 'Whisker High', 'lowerwhisker': 'Whisker Low',
                      'Explained by: Log GDP per capita': 'Economy (GDP per Capita)',
                      'Explained by: Social support': 'Family',
                      'Explained by: Healthy life expectancy': 'Health (Life Expectancy)',
                      'Explained by: Freedom to make life choices': 'Freedom',
                      'Explained by: Perceptions of corruption': 'Trust (Government Corruption)',
                      'Explained by: Generosity': 'Generosity',
                      'Dystopia + residual': 'Dystopia Residual'}, inplace=True)

# add year
csv21['Year'] = yr

# reorder col
csv21 = csv21[['Year', 'Country', 'Region', 'Score', 'SE', 'Whisker High', 'Whisker Low', 'Economy (GDP per Capita)',
               'Family', 'Health (Life Expectancy)', 'Freedom', 'Trust (Government Corruption)', 'Generosity', 'Dystopia Residual']]

print(len(csv21.columns), csv21.columns)  # 14


# read file #
yr = 2022
csv22 = pd.read_csv(f"{path}\\happiness\\{yr}.csv")
# print(len(csv22.columns) + 1, csv22.columns)

# rename col
csv22.rename(columns={'RANK': 'Rank', 'Happiness score': 'Score', 'Whisker-high': 'Whisker High', 'Whisker-low': 'Whisker Low',
                      'Explained by: GDP per capita': 'Economy (GDP per Capita)',
                      'Explained by: Social support': 'Family',
                      'Explained by: Healthy life expectancy': 'Health (Life Expectancy)',
                      'Explained by: Freedom to make life choices': 'Freedom',
                      'Explained by: Perceptions of corruption': 'Trust (Government Corruption)',
                      'Explained by: Generosity': 'Generosity',
                      'Dystopia (1.83) + residual': 'Dystopia Residual'}, inplace=True)

# add year
csv22['Year'] = yr

# reorder col
csv22 = csv22[['Year', 'Country', 'Rank', 'Score', 'Whisker High', 'Whisker Low', 'Economy (GDP per Capita)',
               'Family', 'Health (Life Expectancy)', 'Freedom', 'Trust (Government Corruption)', 'Generosity', 'Dystopia Residual']]

# replace ',' by '.' in value
for col in csv22.columns[6:]:
    csv22[col] = csv22[col].str.replace(',', '.')

print(len(csv22.columns), csv22.columns)  # 13


# Step2) Null Value Check & Rectify
# Before
csv_list = [csv15, csv16, csv17, csv18, csv19, csv20, csv21, csv22]
for csv_file in csv_list:
    print(csv_file['Year'][0])
    for col in csv_file.columns:
        print(col, csv_file[col].isnull().sum())
    print("")

# 2018 1 NA record can replace by 0
csv18['Trust (Government Corruption)'] = csv18['Trust (Government Corruption)'].fillna(0)
# 2022 1 row NA record at the bottom can be deleted
csv22 = csv22[0:-1]

# After
csv_list = [csv15, csv16, csv17, csv18, csv19, csv20, csv21, csv22]
for csv_file in csv_list:
    print(csv_file['Year'][0])
    for col in csv_file.columns:
        print(col, csv_file[col].isnull().sum())
    print("")


# # Step3) create & check df columns to compare
# csv_col_list = [len(csv15.columns), len(csv16.columns), len(csv17.columns), len(csv18.columns),
#                 len(csv19.columns), len(csv20.columns), len(csv21.columns), len(csv22.columns)]
# print(max(csv_col_list))
#
# def append_zeros(csv_file):
#     zeros = [0]*(max(csv_col_list) - len(csv_file.columns))
#     full_cols = csv_file.columns.values.tolist() + zeros
#
#     # print(full_cols)
#     return full_cols
#
# # check df columns to compare
# data = {'2015': append_zeros(csv_file=csv15),
#         '2016': append_zeros(csv_file=csv16),
#         '2017': append_zeros(csv_file=csv17),
#         '2018': append_zeros(csv_file=csv18),
#         '2019': append_zeros(csv_file=csv19),
#         '2020': append_zeros(csv_file=csv20),
#         '2021': append_zeros(csv_file=csv21),
#         '2022': append_zeros(csv_file=csv22)}
#
# df = pd.DataFrame(data)
# df.to_excel("columns.xlsx")


# Step4) Fill the 'missing' columns
csv_rows_list = []
csv_list = [csv15, csv16, csv17, csv18, csv19, csv20, csv21, csv22]
for csv_file in csv_list:
    # print(csv_file.shape[0])
    csv_rows_list.append(csv_file.shape[0])

# csv15 has most rows. i.e. most info. selected to the mapping file
print(max(csv_rows_list), csv_rows_list)

# missing: Region
# unify country name for all csv files
csv16 = csv16.replace({'Country': {'Somaliland Region': 'Somaliland region'}})
csv17 = csv17.replace({'Country': {'Taiwan Province of China': 'Taiwan', 'Hong Kong S.A.R., China': 'Hong Kong'}})
csv18 = csv18.replace({'Country': {'Trinidad & Tobago': 'Trinidad and Tobago', 'Northern Cyprus': 'North Cyprus'}})
csv19 = csv19.replace({'Country': {'Trinidad & Tobago': 'Trinidad and Tobago', 'Northern Cyprus': 'North Cyprus'}})
csv20 = csv20.replace({'Country': {'Taiwan Province of China': 'Taiwan', 'Hong Kong S.A.R. of China': 'Hong Kong'}})
csv21 = csv21.replace({'Country': {'Taiwan Province of China': 'Taiwan', 'Hong Kong S.A.R. of China': 'Hong Kong'}})
csv22["Country"] = csv22["Country"].str.replace('*', '')
csv22 = csv22.replace({'Country': {'Taiwan Province of China': 'Taiwan', 'Hong Kong S.A.R. of China': 'Hong Kong',
                                   'Congo': 'Congo (Kinshasa)', 'Czechia': 'Czech Republic',
                                   'Eswatini, Kingdom of': 'Swaziland'}})


# drop out 'Region' col that is originally available in csvs as some names in 'Region' are different
csv16 = csv16.drop('Region', axis=1)
csv20 = csv20.drop('Region', axis=1)
csv21 = csv21.drop('Region', axis=1)


csv_list = []
df_source_fm = csv15
df_source_to_list = [csv16, csv17, csv18, csv19, csv20, csv21, csv22]

for df_source_to in df_source_to_list:
    result = pd.merge(df_source_to, df_source_fm[['Country', 'Region']], on='Country', how='left')
    csv_list.append(result)

# assign the csv variable name again
csv16, csv17, csv18, csv19, csv20, csv21, csv22 = csv_list


csv_list = [csv16, csv17, csv18, csv19, csv20, csv21, csv22]
for csv_file in csv_list:
    print(csv_file['Region'].isnull().sum())


# check missing value
print('Before')
csv_list = [csv16, csv17, csv18, csv19, csv20, csv21, csv22]
for csv_file in csv_list:
    missing_countries = csv_file.query('Region.isnull()')['Country'].values.tolist()
    print(missing_countries)


# fill in region for missing country
def fix_region(csv_list, c_place, r_place):
    csv_list_fixed = []
    for csv_file in csv_list:
        csv_file.loc[csv_file['Country'] == c_place, 'Region'] = r_place
        csv_list_fixed.append(csv_file)
    return csv_list_fixed

fix_region(csv_list=[csv16], c_place='Puerto Rico', r_place='Latin America and Caribbean')
fix_region(csv_list=[csv16, csv17, csv18], c_place='Belize', r_place='Central America')
fix_region(csv_list=[csv16, csv17, csv18, csv19], c_place='Somalia', r_place='Horn of Africa')
fix_region(csv_list=[csv16, csv17, csv18, csv19, csv20, csv21, csv22], c_place='Namibia', r_place='Southeast Africa')
fix_region(csv_list=[csv16, csv17, csv18, csv19, csv20], c_place='South Sudan', r_place='Eastern Central Africa')
fix_region(csv_list=[csv19, csv20, csv21, csv22], c_place='Gambia', r_place='Western Africa')
fix_region(csv_list=[csv19, csv21, csv22], c_place='North Macedonia', r_place='Southeast Europe')
fix_region(csv_list=[csv20, csv21], c_place='Maldives', r_place='Southern Asia')

# check missing value
print('After')
csv_list = [csv16, csv17, csv18, csv19, csv20, csv21, csv22]
for csv_file in csv_list:
    missing_countries = csv_file.query('Region.isnull()')['Country'].values.tolist()
    print(missing_countries)



# missing: Rank
df20 = csv20
df20['Rank'] = df20['Score'].rank(ascending=False)
df21 = csv21
df21['Rank'] = df21['Score'].rank(ascending=False)

# missing: Dystopia Residual
df18 = csv18
df18['Dystopia Residual'] = df18['Score'] - df18['Economy (GDP per Capita)'] - df18['Family'] - \
                            df18['Health (Life Expectancy)'] - df18['Freedom'] - df18['Trust (Government Corruption)'] \
                            - df18['Generosity']
df19 = csv19
df19['Dystopia Residual'] = df19['Score'] - df19['Economy (GDP per Capita)'] - df19['Family'] - \
                            df19['Health (Life Expectancy)'] - df19['Freedom'] - df19['Trust (Government Corruption)'] \
                            - df19['Generosity']


# work on longitude and latitude for plot graph
ll_df = pd.read_excel(f"{path}\\happiness\\countries.xlsx")
ll_df.rename(columns={'country': 'Fips', 'name': 'Country', 'latitude': 'Latitude', 'longitude': 'Longitude'}, inplace=True)

# fix naming of country in countries.xlsx
def fix_country(c_place_ori, c_place_new):
    ll_df.loc[ll_df['Country'] == c_place_ori, 'Country'] = c_place_new
    return ll_df

country_dict = {'Somalia': 'Somaliland region', 'Macedonia [FYROM]': 'Macedonia', 'Myanmar [Burma]': 'Myanmar',
                'Congo [DRC]': 'Congo (Brazzaville)', 'Congo [Republic]': 'Congo (Kinshasa)', "Côte d'Ivoire": 'Ivory Coast'}

for key, val in country_dict.items():
    fix_country(c_place_ori=key, c_place_new=val)



# append countries info to countries.xlsx
print(ll_df.shape)  # (246, 4)  # 'Fips', 'Latitude', 'Longitude', 'Country'
data = [['', 35.248, 33.6577, 'North Cyprus'], ['', 5.1521, 46.1996, 'Somalia'],
        ['', 6.8770, 31.3070, 'South Sudan'], ['', 41.6086, 21.7453, 'North Macedonia']]
ll_df2 = pd.DataFrame(data, columns=['Fips', 'Latitude', 'Longitude', 'Country'])

ll_df = pd.concat([ll_df, ll_df2], ignore_index=True, axis=0)
print(ll_df.shape)


# append longitude and latitude info
csv_list = []
df_source_fm = ll_df
df_source_to_list = [csv15, csv16, csv17, csv18, csv19, csv20, csv21, csv22]

for df_source_to in df_source_to_list:
    result = pd.merge(df_source_to, df_source_fm[['Country', 'Latitude', 'Longitude']], on='Country', how='left')
    csv_list.append(result)

# assign the csv variable name again
csv15, csv16, csv17, csv18, csv19, csv20, csv21, csv22 = csv_list


# check missing value
csv_list = [csv15, csv16, csv17, csv18, csv19, csv20, csv21, csv22]
for csv_file in csv_list:
    missing_longitude = csv_file.query('Longitude.isnull()')['Country'].values.tolist()
    missing_latitude = csv_file.query('Latitude.isnull()')['Country'].values.tolist()
    print(missing_longitude)
    print(missing_latitude)


# create size according to ranking for plot graph
def select_size(row):
    if 0 <= row["Rank"] <= 20:
        return 17
    elif 21 <= row["Rank"] <= 40:
        return 14
    elif 41 <= row["Rank"] <= 60:
        return 11
    elif 61 <= row["Rank"] <= 80:
        return 10
    elif 81 <= row["Rank"] <= 100:
        return 9
    elif 101 <= row["Rank"] <= 120:
        return 7
    elif 121 <= row["Rank"] <= 140:
        return 6
    elif 141 <= row["Rank"]:
        return 5

csv_list = [csv15, csv16, csv17, csv18, csv19, csv20, csv21, csv22]
for csv_file in csv_list:
    csv_file['Size'] = csv_file.apply(lambda row: select_size(row), axis=1)


# create continent column
''' 5 continents are Africa, Europe, Asia, America, and Oceania '''
asia_r_list = ["Southern Asia", "Southeastern Asia", "Eastern Asia"]
europe_r_list = ["Central and Eastern Europe", "Western Europe", "Southeast Europe"]
africa_r_list = ["Middle East and Northern Africa", "Sub-Saharan Africa", "Southeast Africa",
                 "Horn of Africa", "Eastern Central Africa", "Western Africa"]
n_america_r_list = ["North America", "Central America"]
s_america_r_list = ["Latin America and Caribbean"]
oceania_r_list = ["Australia and New Zealand"]
continent_names_list = ['Asia', 'Europe', 'Africa', 'North America', 'South America', 'Oceania']

def create_continent(row):
    if row["Region"] in asia_r_list:
        return continent_names_list[0]
    elif row["Region"] in europe_r_list:
        return continent_names_list[1]
    elif row["Region"] in africa_r_list:
        return continent_names_list[2]
    elif row["Region"] in n_america_r_list:
        return continent_names_list[3]
    elif row["Region"] in s_america_r_list:
        return continent_names_list[4]
    elif row["Region"] in oceania_r_list:
        return continent_names_list[5]


csv_list = [csv15, csv16, csv17, csv18, csv19, csv20, csv21, csv22]
for csv_file in csv_list:
    csv_file['Continent'] = csv_file.apply(lambda row: create_continent(row), axis=1)


# Step5) remove SE, CI, Whisker columns & reorder columns
# Definitions
# Standard Error: the standard deviation of its sampling distribution or an estimate of that standard deviation
# Confidence Interval: sample mean ± margin of error. Upper & Lower bounds are the range to fall between
# Whisker: The upper & lower whiskers represent scores outside the middle 50% of quartile
# (i.e., the lower 25% of scores and the upper 25% of scores)

final_cols = ['Year', 'Country', 'Region', 'Rank', 'Score', 'Economy (GDP per Capita)', 'Family',
              'Health (Life Expectancy)', 'Freedom', 'Trust (Government Corruption)', 'Generosity', 'Dystopia Residual',
              'Latitude', 'Longitude', 'Size', 'Continent']


# trim cols and save as csv
csv_list = [csv15, csv16, csv17, csv18, csv19, csv20, csv21, csv22]
file_yr_list = list(range(15, 23, 1))
for csv_file, file_yr in zip(csv_list, file_yr_list):
    csv_file = csv_file[final_cols]
    print(len(csv_file.columns), csv_file.columns)
    csv_file.to_csv(f"{path}\\updated\\20{file_yr}n.csv", index=False)


# Step6) create a new master file with only year & ranking
csv_list = [csv15, csv16, csv17, csv18, csv19, csv20, csv21, csv22]
df_concat = pd.concat(csv_list, axis=0)
df_concat = df_concat.sort_values(by=['Country', 'Year'], ascending=True)
print(df_concat.head(10))
df_concat.to_csv('df_concat.csv', index=False)

# rank15 = csv15[['Country', 'Region', 'Rank', 'Score', 'Year']]
# print(rank15.head(5))

