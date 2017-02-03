library(darksky)
library(purrr)
darksky_api_key()
x = get_forecast_for(49.840, -95.150, "2016-05-08T03:10:00", add_headers=TRUE)
x = as.data.frame(x)

