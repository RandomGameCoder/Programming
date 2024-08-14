# Load required packages
library(stats)

x1 = rnorm(100)
x2 = rnorm(100)
y = 2*x1 + 3*x2 + rnorm(100)

# Create sample data
set.seed(123)
data <- data.frame(x1,x2,y)
data

# Build linear model
model <- lm(y ~ x1 + x2, data = data)

# Predict values
predicted <- predict(model, newdata = data)
print(predicted)

# Analyze the fit
print(summary(model))
plot(model, which = 1)
plot(model, which = 2)
plot(model, which = 5)