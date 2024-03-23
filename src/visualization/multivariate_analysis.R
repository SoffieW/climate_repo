library(dplyr)
library(tidyr)
library(ggplot2)
library(GGally)
library()

path = file.path(getwd(), '..', '..', 'data', 'interim')
print(path)

df = read.csv(paste0(path, '/multivariable.csv'))

# Need to remove trendline from temperature data in order to compare to el nino and la nina indices.


df %>% 
  mutate_if(is.character, as.numeric) %>% 
  mutate(mean_nn = (DJF_y + MAM_y + JJA_y + SON_y)/4) %>% 
  mutate(mean_temp = (DJF_x + MAM_x + JJA_x + SON_x)/4) %>% 
  ggplot(aes(x = Year, y = mean_temp)) +
  geom_line()

dcmp <- df %>% 
  mutate_if(is.character, as.numeric) %>% 
  mutate(mean_nn = (DJF_y + MAM_y + JJA_y + SON_y)/4) %>% 
  mutate(mean_temp = (DJF_x + MAM_x + JJA_x + SON_x)/4) %>% 
  model(stl = STL(mean_temp))

df %>% 
  mutate_if(is.character, as.numeric) %>% 
  mutate(mean_nn = (DJF_y + MAM_y + JJA_y + SON_y)/4) %>% 
  mutate(mean_temp = (DJF_x + MAM_x + JJA_x + SON_x)/4) %>% 
  na.omit() -> df1

# set up stl function
fit <- stl(df1 %>% 
             select(mean_temp), s.window = "periodic")

# plot stl
library(ggfortify)
autoplot(fit)