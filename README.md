# Determining the best location for physical store using customer's data.

## Intro

I am tasked with helping CityCorp, a fictional company, decide on the optimal locations to open three new stores in the UK. These stores will cater to Men, Women, and Children, respectively. CityCorp currently operates online and intends to expand its presence by strategically selecting the best physical locations based on trading data.

My role involves using a proximity algorithm to assess the potential success of each type of store at the provided locations. To achieve this, I will need to develop a function for calculating the distance between two points based on their latitude and longitude coordinates. I will then employ this function to assign weights to each potential sale, taking into account its distance from the candidate location. Ultimately, my goal is to determine the most suitable location for each store type based on these proximity-weighted factors.

## Steps

**Part 1: Implement the Haversine Formula**
To begin, we need to create a Python function that converts latitude and longitude coordinates into distances using the Haversine formula. You can find details of this formula [here](https://www.movable-type.co.uk/scripts/latlong.html). This function should use appropriate trigonometric functions, such as `atan2`. It's essential to test this function with known values to ensure accuracy. You can use the online tool provided in the link above to verify your implementation.

**Part 2: Calculate Estimated Income**
Once we have the distance calculation function ready, we will use it to calculate the estimated income for each store location and type of customer (Men, Women, Children). To do this, we will need a file, such as "AccountLocation.xlsx" (or "Backup.xlsx" if the former is unavailable). Ensure that you convert latitude and longitude values from the file into floating-point numbers.
The code should:
- Read the location and type-based values from the Excel file.
- Calculate the probability of each customer visiting each store location based on distance.
- Multiply the value by the type for each location by the probability of a customer visiting that location.
- Sum the income estimates over all customer accounts.
The result should be saved in a file called "Income.xlsx," where each row represents a possible store location from "locations.xlsx." The first column should contain the location name, and columns two to four should contain the estimated income for Men, Women, and Children, respectively.

**Part 3: Find Optimal Store Locations**
To maximize total estimated income, we need to ensure that the three stores are located in different places. You can achieve this by:
- Reading the "Income.xlsx" file to get the income estimates for each store location.
- Implementing a strategy (e.g., greedy algorithm or optimization algorithm) to select three distinct store locations that maximize the total estimated income.
- Printing a message to the console indicating where the three stores should be located for maximum income.

## Summary

