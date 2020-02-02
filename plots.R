library(ggplot2)
library(dplyr)


data = read.csv("gs_income_demo_clean.csv", stringsAsFactors=FALSE)
data = data[complete.cases(data), ]
head(data)

# Average RATINGS by school type and location
group_type_is_nyc = data %>% 
  mutate(is_nyc = ifelse(is_nyc=='nyc', 'NYC','Not in NYC')) %>% 
  group_by(is_nyc, type) %>%
  summarize(mean(rating)) %>%
  arrange(desc(`mean(rating)`))
head(group_type_is_nyc)

g = ggplot(group_type_is_nyc, aes(type, `mean(rating)`))
g + geom_col(aes(fill=is_nyc), position='dodge') +
  ggtitle('Average School Rating by School Type and Location') +
  labs(x='School Type', y='Average Rating', fill='Location') +
  scale_fill_manual(values=c('#002649', '#355e3b')) +
  coord_cartesian(ylim = c(3, 6.5)) +
  geom_text(aes(label=round(`mean(rating)`, digits = 2), size=3), vjust=2,
            hjust=c(-1.75,2.75,-1.75,2.75), size=3.25, color= 'white', fontface='bold')
 
  

# Median INCOME by school type and location
group_income_is_nyc = data %>% 
  mutate(is_nyc = ifelse(is_nyc=='nyc', 'NYC','Not in NYC')) %>% 
  group_by(is_nyc, type) %>%
  summarize(median(income_per_household)) %>%
  arrange(desc(`median(income_per_household)`))
head(group_income_is_nyc)


h = ggplot(group_income_is_nyc, aes(type, `median(income_per_household)`))
h + geom_col(aes(fill=is_nyc), position='dodge') +
  ggtitle('Median Income by School Type and Location') +
  labs(x='School Type', y='Median Household Income ($)', fill='Location') +
  scale_fill_manual(values=c('#002649', '#355e3b')) +
  coord_cartesian(ylim = c(30000, 70000)) +
  geom_text(aes(label=round(`median(income_per_household)`, digits = -2), size=3),
            vjust=c(2,2,2,2), hjust=c(2,-1,-1,2), size=3.25, color= 'white', fontface='bold')


# DEMOGRAPHICS MEDIAN by school type and location
group_demo_is_nyc = data %>% 
  mutate(is_nyc = ifelse(is_nyc=='nyc', 'NYC','Not in NYC')) %>% 
  group_by(is_nyc, type) %>%
  summarize(median(per_african_american)) %>%
  mutate(median_ = `median(per_african_american)`*100) %>% 
  arrange(desc(median_))
head(group_demo_is_nyc)


j = ggplot(group_demo_is_nyc, aes(type, median_))
j + geom_col(aes(fill=is_nyc), position='dodge') +
  ggtitle('Demographics by School Type and Location') +
  labs(x='School Type', y='Median Percent African American', fill='Location') +
  scale_fill_manual(values=c('#002649', '#355e3b')) +
  coord_cartesian(ylim = c(0, 50)) +
  geom_text(aes(label=round(median_, digits = 0), size=3), vjust=c(2,2,2,1.25),
            hjust=c(-3.5,4.5,-3.5,8), size=3.25, color= 'white', fontface='bold')




# DEMOGRAPHICS MEAN by school type and location
group_demo_is_nyc = data %>% 
  mutate(is_nyc = ifelse(is_nyc=='nyc', 'NYC','Not in NYC')) %>% 
  group_by(is_nyc, type) %>%
  summarize(mean(per_african_american)) %>%
  mutate(mean_ = `mean(per_african_american)`*100) %>% 
  arrange(desc(mean_))
head(group_demo_is_nyc)


k = ggplot(group_demo_is_nyc, aes(type, mean_))
k + geom_col(aes(fill=is_nyc), position='dodge') +
  ggtitle('Demographics by School Type and Location') +
  labs(x='School Type', y='Aveage Percent African American', fill='Location') +
  scale_fill_manual(values=c('#002649', '#355e3b')) +
  coord_cartesian(ylim = c(0, 50)) +
  geom_text(aes(label=round(mean_, digits = 0), size=3), vjust=c(2,2,2,2),
            hjust=c(-3.5,4.5,-3.5,8), size=3.25, color= 'white', fontface='bold')


  





