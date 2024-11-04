## Description

The policy which determines the new rolling mean.
## Called By
## Domain Spaces
1. [[Sample Space]]
## Followed By
## Codomain Spaces
1. [[Mean Space]]
2. [[Sample Queue Space]]
## Constraints
## Parameters Used
1. [[Rolling Mean Window]]
## Metrics Used
## Policy Options
### 1. Update Rolling Mean Policy V1
#### Description
Simple policy which computes the rolling mean based on a maximum rolling mean window
#### Logic
1. Compute sum as the state variable of current mean times the length of the sample queue state variable
2. Add the sample from DOMAIN[0] to this value and append it to the sample queue
3. If the sample queue length is greater than PARAMS['Rolling Mean Window'] then pop the first element in the queue and subtract it from the sum
4. Divide the sum by the legnth of samples and return the two spaces

