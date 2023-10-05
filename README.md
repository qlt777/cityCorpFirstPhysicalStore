# Determining the best location for physical store using customer's data.
##Task Summary:
CityCorp, a fictional company, wanted to determine the optimal locations for opening three new stores in the UK catering to Men, Women, and Children. The goal was to expand their online presence by strategically selecting physical store locations based on trading data.
##Approach:
1. **Distance Calculation Function:** Developed a Python function using the Haversine formula to calculate the distance between two points given their latitude and longitude coordinates. The Haversine formula accounts for the Earth's curvature when calculating distances.
2. **Estimated Income Calculation:** Utilized the Haversine distance function to read data from the "AccountLocation.xlsx" file. For each potential store location, estimated income was calculated by multiplying the value for each type (Men, Women, Children) by the probability that a customer would visit based on the straight-line distance.
3. **Output File Creation:** Generated a new Excel file named "Income.xlsx" containing rows for each possible store location from the "locations.xlsx" file. The columns included the estimated income for Men, Women, and Children.
4. **Optimal Store Location Determination:** To find the optimal store locations that maximize total estimated income while ensuring that the three stores were in different locations, an analysis of the "Income.xlsx" file was conducted.
   - Store locations were sorted by income for each category (Men, Women, Children).
   - Three store locations were selected, ensuring they were different and had the highest income in each category.
   - The total estimated income for the chosen store locations was calculated.
5. **Results:** The selected optimal store locations and the total estimated income were printed to the console.

This approach allowed CityCorp to make data-driven decisions regarding the placement of their new stores for maximum potential revenue.
