# Exploratory Data Analysis (EDA) in R

# Step 1: Load dataset
# Replace 'data.csv' with your dataset
data <- read.csv("data.csv")

cat("First 5 rows:\n")
head(data)

# Step 2: Structure of dataset
cat("\nStructure of dataset:\n")
str(data)

# Step 3: Statistical summary
cat("\nSummary statistics:\n")
summary(data)

# Step 4: Check missing values
cat("\nMissing values in each column:\n")
colSums(is.na(data))

# Step 5: Replace missing values with mean
for(i in 1:ncol(data)){
  if(is.numeric(data[,i])){
    data[is.na(data[,i]), i] <- mean(data[,i], na.rm=TRUE)
  }
}

cat("\nMissing values handled.\n")

# Step 6: Correlation matrix
numeric_data <- data[sapply(data, is.numeric)]
cat("\nCorrelation matrix:\n")
cor(numeric_data)

# Step 7: Histogram
hist(numeric_data[,1], main="Histogram", col="skyblue")

# Step 8: Boxplot
boxplot(numeric_data, main="Boxplot for Outliers", col="orange")

# Step 9: Scatter plot (first two numeric columns)
if(ncol(numeric_data) >= 2){
  plot(numeric_data[,1], numeric_data[,2],
       main="Scatter Plot",
       xlab="Feature 1",
       ylab="Feature 2",
       col="blue",
       pch=19)
}

cat("\nEDA Completed Successfully ✅\n")