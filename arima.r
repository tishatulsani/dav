# Load dataset
data <- read.csv("timeseries.csv")

# Convert to time series
ts_data <- ts(data$value, frequency = 12)

# Fit ARIMA model
model <- arima(ts_data, order = c(1,1,1))

# Forecast
forecast <- predict(model, n.ahead = 5)

# Print forecast values (NEW)
print(forecast$pred)

# Plot
plot(ts_data, col="black", main="ARIMA Forecast (R)", ylab="Value", xlab="Time")

lines(forecast$pred, col="red")

# Add legend (NEW)
legend("topleft", legend=c("Original", "Forecast"),
       col=c("black","red"), lty=1)

grid()  # NEW