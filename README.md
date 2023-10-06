# Determining the best location for physical store using customer's data.

## Intro

I am tasked with helping CityCorp, a fictional company, decide on the optimal locations to open three new stores in the UK. These stores will cater to Men, Women, and Children, respectively. CityCorp currently operates online and intends to expand its presence by strategically selecting the best physical locations based on trading data.

My role involves using a proximity algorithm to assess the potential success of each type of store at the provided locations. To achieve this, I will need to develop a function for calculating the distance between two points based on their latitude and longitude coordinates. I will then employ this function to assign weights to each potential sale, taking into account its distance from the candidate location. Ultimately, my goal is to determine the most suitable location for each store type based on these proximity-weighted factors.

## Steps

**Part 1: Implementing the Haversine Formula**

To kick off this project, I needed to create a Python function capable of converting latitude and longitude coordinates into distances using the Haversine formula. I found detailed information about this formula on a [helpful webpage](https://www.movable-type.co.uk/scripts/latlong.html). For the implementation, I utilized suitable trigonometric functions, including atan2. To ensure the accuracy of my function, I performed rigorous testing using known values. I even used the online tool provided in the link above to validate my implementation.

**Part 2: Calculating Estimated Income**

With the distance calculation function ready, the next step was to estimate the income for each store location, considering different customer types (Men, Women, Children). I relied on data from an Excel file, "AccountLocation.xlsx" (or "Backup.xlsx" if the former wasn't available). It was crucial to convert latitude and longitude values from this file into floating-point numbers. The code for this part encompassed the following steps:
1. Reading location and type-based values from the Excel file.
2. Calculating the probability of a customer visiting each store location based on the distance.
3. Multiplying the value by the customer type for each location by the probability of a customer visiting that location.
4. Summing up the income estimates over all customer accounts.
5. The final result was stored in a file named "Income.xlsx." In this file, each row represented a possible store location from the "locations.xlsx" data. The first column contained the location name, while columns two to four held the estimated income for Men, Women, and Children, respectively.

**Part 3: Finding Optimal Store Locations**

To maximize the total estimated income, it was vital to ensure that the three stores were strategically placed in different areas. I accomplished this task by:
1. Reading the "Income.xlsx" file to access the income estimates for each store location.
2. Implementing a selection strategy, which could be a greedy algorithm or an optimization algorithm. This strategy aimed to choose three distinct store locations that would maximize the total estimated income.
3. Finally, I printed a message to the console indicating the optimal locations for the three stores to achieve the highest income.

## Summary

