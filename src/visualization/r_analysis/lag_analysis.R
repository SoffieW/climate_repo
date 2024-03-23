library(dplyr)
library(ggplot2)
library(tidyr)
library(GGally)
library(tsibble)
library(feasts)
library(lubridate)

# read in timeseries file from interim data directory
path = file.path(getwd(), '..', '..', '..', 'data', 'interim', 'df_main.csv')
print(path)
df = read.csv(path)

# turns csv into tsibble, with index: Year-Month
df %>% 
  mutate(Date = yearmonth(Year.Month)) %>% 
  as_tsibble(index = Date) -> temps

# run this code to generate seasonal plot
temps %>% 
  gg_season(Value)

# run this code to generate visual: timeseries plot
temps %>% 
  filter(year(Date) >=2015) %>% 
  autoplot(Value) 

# run this code to generate visual: lag plots
temps %>% 
  filter(year(Date) >=2015) %>% 
  gg_lag(Value, geom= "point", lags = 1:12) +
  labs(x = "lag(Temp (\u00B0C), k)", y= "Temp (\u00B0C)") +
  ggtitle("Lag plots of Global Mean Monthly Temp")

# run this code to generate visual: autocorrelation plot
temps %>% 
  ACF(Value, lag_max = 120) %>% 
  autoplot() + 
  ggtitle("Autocorrelation of Temperature over 60 Months")

dcmp <- temps %>% 
  filter(year(Year.Month) >= 2000) %>% 
  model(stl = STL(Value))

components <-components(dcmp)

components %>% 
  as_tsibble() %>% 
  autoplot(Value, colour="gray") +
  geom_line(aes(y=trend), colour = "#D55E00") +
  labs(
    y = "Temperature Anomaly",
    title = "Global Monthly Mean Surface Temperature"
  ) -> stl_dcmp_plot


plot_path = file.path(getwd(), '..', '..', '..', 'reports', 'figures')

ggsave(path = plot_path, stl_dcmp_plot, filename = "myplot.png")

components %>% autoplot()