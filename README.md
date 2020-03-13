# ourStatsProject
[![Build Status](https://travis-ci.com/Darsh374/ourStatsProject.svg?branch=master)](https://travis-ci.com/Darsh374/ourStatsProject)


Calculator Object
1.	Properties
1.	Result 
2.	Methods
1.	Addition -> Calls addition static method from Calculator
2.	Subtraction -> Call subtraction static method from Calculator
3.	Multiplication -> Calls multiplication static method from Calculator
4.	Division -> Calls division static method from Calculator
5.	Root -> Calls root static method from Calculator
6.	Power -> Calls power static method from Calculator
3.	Calculator Static Class
1.	Methods
1.	Addition -> Calls addition class method of sum
2.	Subtraction->Calls subtraction class method of difference
3.	Multiplication -> Calls multiplication class method of product
4.	Division -> Calls division class method of division
5.	Root -> Calls root class method of root
6.	Power -> Calls power class method power
4.	Operations class(s)
1.	Addition
1.	Methods 
1.	Sum 1 numbers
2.	Sum List of numbers
2.	Subtraction
1.	Methods
1.	Subtract 2 numbers
3.	Multiplication
1.	Methods
1.	Multiplies two numbers
4.	Division
1.	Methods
1.	Divides two numbers
5.	Root
1.	Methods
1.	Finds the nth root of a number
6.	Power
1.	Methods
1.	Finds the nth power of a number
Statistics Object
1.	Properties
1.	Result 
2.	Methods
1.	Mean -> Calls mean static method from Statistics
2.	Median -> Call median static method from Statistics
3.	Mode -> Calls mode static method from Statistics
4.	Variance -> Calls variance static method from Statistics
5.	Standard Deviation -> Calls standard deviation static method from Statistics
6.	Quartiles -> Calls quartile static method from Statistics
7.	Skewness -> Calls skewness static method from Statistics
8.	Sample Correlation -> calls sample correlation static method from Statistics
9.	Population Correlation -> calls population correlation static method from Statistics
10.	 Z-score -> calls zScore static method from statistics
11.	Mean Deviation -> calls meanDeviation static method from statistics
3.	Statistics Class
1.	Methods
1.	Mean -> Calls mean class method of mean
2.	Median -> Calls median class method of median
3.	Mode -> Calls mode class method of mode
4.	Variance -> Calls variance class method of variance
5.	Standard Deviation -> Calls standard Deviation class method of standard_deviation
6.	Quartiles -> Calls quartiles class method of quartile
7.	Skewness -> Calls skewness class method of skewness
8.	Sample Correlation -> calls sample correlation class method of sample_correlation
9.	Population Correlation -> calls population correlation class method of pop_correlation
10.	 Z-score -> calls zscore class method of zScore
11.	 Mean Deviation -> calls mean deviation class method of meanDeviation
4.	Operations class(s)
1.	Mean
1.	Methods
1.	Adds up a list 
2.	Divides by number of values
2.	Median
1.	Methods
1.	Sorts a list from smallest to largest
2.	Picks the middle number or divides the two middle ones by two
3.	Mode
1.	Methods
1.	Finds the number in the list that has been repeated the most
4.	Variance
1.	Methods
1.	Finds the variance of a set of data
5.	Standard Deviation
1.	Methods
1.	Finds the standard deviation of a set of data
6.	Quartiles
1.	Methods
1.	Finds Q1
2.	Finds Q2
3.	Finds Q3
7.	Skewness
1.	Methods
1.	Finds the skewness of a set of data
8.	Sample Correlation
1.	Methods
1.	Finds the correlation of sample
9.	Population Correlation
1.	Methods
1.	Finds the sample size
2.	Finds the correlation of the sample
10.	Z-score
1.	Methods
1.	Finds the z-score
11.	 Mean Deviation
1.	Methods
1.	Finds the how the mean deviates
PopulationSampling Object
1.	Properties
-	Result
2.	PopulationSampling Class
-	Simple Random Sampling -> Calls simple random class method of simpleRandomSample
-	Systematic Sampling -> calls systematic sampling class method of systematicSampling
-	Confidence Interval for a Sample -> calls confidence class method of confidence
-	Margin of Error -> call margin of error class method of margin_error
-	Cochran’s Sample size Formula -> calls sample size class method of sample_size
-	How to Find a Sample Size Given a Confidence Interval and Width (unknown population standard deviation) -> calls sample size uknown class method of SampleSizeUnknownPop
-	How to Find a Sample Size Given a Confidence Interval and Width (known population standard deviation) ->calls sample size known class method of SampleSizeKnownPop
(3)	Methods
-	Simple Random Sampling -> Call simpleRandomSample static method from PopulationSampling
-	Systematic Sampling -> Calls systematicSample static method from PopulationSampling
-	Confidence Interval for a Sample -> Calls confidence static method from PopulationSampling
-	Margin of Error -> Call margin_error static method from PopulationSampling
-	Cochrans Sample Size Formula -> Call sample_size static method from PopulationSampling
-	How to Find a Sample Size Given a Confidence Interval and Width (unknown population standard deviation) -> Call sample_size_uknown static method from PopulationSampling
-	How to Find a Sample Size Given a Confidence Interval and Width (known population standard deviation) -> Call sample_size_known static method from PopulationSampling
4-Operations class(s)
-	Simple Random Sampling 
Methods:
		1. finds the sample size
-	Systematic Sampling 
Methods:
	1. finds the sample systematically
	2.gets the nth number from a list 
	3. appends to the new list
-	Confidence Interval for a Sample 
Methods:
	1.finds the confidence for sample size
-	Margin of Error 
Methods:
	1.
-	Cochrans Sample Size Formula 
Methods:
	1.calculates the sample size
-	How to Find a Sample Size Given a Confidence Interval and Width (unknown population standard deviation) 
Methods:
1.calculates the sample size without standard deviation given width
-	How to Find a Sample Size Given a Confidence Interval and Width (known population standard deviation) 
Methods:
1. calculates the sample size given the population standard deviation with width


RandomNum Object
1. Properties
	- Result
2. RandomNums Class
- Generate a random number without a seed between a range of two numbers - Both Integer and Decimal -> Calls RandIntNoSeed class method of RandIntNoSeed & calls RandDecNoSeed class method of RandDecNoSeed
- Generate a random number with a seed between a range of two numbers - Both Integer and Decimal -> Calls RandIntSeed class method of RandIntSeed & calls RandDecSeed class method of RandDecSeed
- Generate a list of N random numbers with a seed and between a range of numbers - Both Integer and Decimal -> Calls RangeNums class method of RangeNums
- Select a random item from a list ->Calls RandomItem class method of RandomItem
- Set a seed and randomly.select the same value from a list -> Calls RandomSelect class method of RandomSelect
- Select N number of items from a list without a seed -> Calls NItemsNoSeed class method of NItemsNoSeed
- Select N number of items from a list with a seed -> Calls NItemsSeed class method of NItemsSeed
3. Methods
- Generate a random number without a seed between a range of two numbers - Both Integer and Decimal -> Calls RandIntNoSeed static method from RandomNums / Calls RandDecNoSeed static method from RandomNums
- Generate a random number with a seed between a range of two numbers - Both Integer and Decimal -> Calls RandIntSeed static method from RandomNums / Calls RandDecSeed static method from RandomNums
- Generate a list of N random numbers with a seed and between a range of numbers - Both Integer and Decimal -> Calls RangeNums static method from RandomNums
- Select a random item from a list -> Calls RandomItem static method from RandomNums
- Set a seed and randomly.select the same value from a list -> Calls RandomSelect static method from RandomNums
- Select N number of items from a list without a seed -> Calls NItemsNoSeed static method from RandomNums
- Select N number of items from a list with a seed -> Calls NItemsSeed static method from RandomNums
4. Operations Class
- Generate a random number without a seed between a range of two numbers - Both Integer and Decimal -> RandIntNoSeed / RandDecNoSeed
- Generate a random number with a seed between a range of two numbers - Both Integer and Decimal -> RandIntSeed / RandDecSeed
- Generate a list of N random numbers with a seed and between a range of numbers - Both Integer and Decimal -> RangeNums
- Select a random item from a list -> RandomItem
- Set a seed and randomly.select the same value from a list -> RandomSelect
- Select N number of items from a list without a seed -> NItemsNoSeed
- Select N number of items from a list with a seed -> NItemsSeed















