ABSTRACT

Guaranteeing food profit may be a vital issue agriculture dependent nations like India, wherever over thirty third of the folks earn their financial gain directly or indirectly supported a selected yield .Estimating and evaluating the yield of crops is finished globally to supply high yield and also the acceptable price. However to estimate the price there's no correct procedure in situ for providing insight to farmers on what crops area unit to be full-grown. Hence, during this paper we've got tried to predict the value of crops that a farmer will get from his land, by analyzing patterns in past information. we've got thought of few rabi and kharif season crops for our analysis. we tend to build use of many information like precipitation, temperature, market costs, space of land and past yield of a crop. during this project, we tend to implement many supervised machine learning algorithms and analyse the info and predict the end result for the new set of information.

INTRODUCTION

In the current situation, the govt. is aggregation information solely in its raw kind, and this information is of no use to the tip user, that's the farmers. aggregation this information, standardizing it, analyzing it, and feeding it to a system which will offer relative trends is that the aim of our project.
These relative trends can act as solutions for farmers, particularly in drought afflicted areas. for instance, the cultivation of Kharif Rice is resource intensive and will be solely wiped out a precipitation made amount, otherwise it may deplete the natural reserves of H2O, resulting in deficiency within the formation, that consequently ends up in drought like conditions. this instance, as naïve because it might sound, represents a broad category of trends that once figure with efficiency victimization the prevailing data processing algorithms, will turn out a excess of solutions, that once adhered to, can facilitate alleviate the same drought like conditions.
Another example can be of the crop Rabi Maize. Rabi crops or Rabi harvest area unit agricultural crops seeded in winter and harvested within the spring. The Rabi crops area unit seeded around mid- November, when the monsoon rains area unit over, and gathering begins within the months of Gregorian calendar month or might. The crops area unit full-grown either with rain that has percolated into the bottom, or with irrigation. a decent rain in winter spoils the Rabi crops however is nice for kharif crops. Our project aims at distinctive specific area unitas that are appropriate for specific crops, therefore on avoid deficit of crops.
If you verify these examples, you'll see that the number of precipitation that happens in a district, the crop made therein space, the season and alternative such parameters, area unit all correlative and might kind trends which will provide U.S.A. solutions for appropriate farming practices which will facilitate farmers with success avoid drought-like things.
The ultimate objective of this project is to square as a system that once fed with information relating to numerous parameters, with success produces trends and correlations which will facilitate the user of the system develop solutions to tackle or minimize the harm of drought. mechanization of this method can drastically cut back the time needed to review patterns and perform in depth analysis to get reports, and can provides a shut estimation of the specified outcome.

LITERATURE SURVEY
 
Nowadays, several researchers have enforced many models to predict crop yield predictions. But these models have many drawbacks because of the inaccurate use of the algorithms.

In [2], a prognostic model is projected to spot the crop yield employing a Hybrid neural network considering the soil parameters and therefore the external climate conditions. however the model fails to predict for the important time fluctuations within the climate and soil parameters.Hence the model will suit for time period analysis.
In [3], A Prediction system is developed victimisation KNN and Apriori formula to analyse and suggest the crops to the farmers. The system features a well-developed Interface to input crop, that permits the user to input the crop names and that it outputs the crop yield. however the system doesn't have the supply to prediction worth at
the same time.
In [4], an automatic farming crops prediction system is developed victimization KNN formula and Multi-linear regression for People's Republic of Bangladesh countries. however the model is taken into account to be Associate in Nursing initial step within the advancement since it
does not determine any new analysis gaps.
In [5], The system is meant to predict crop yield and therefore the chemical recommendation that can be used for analysis soil and therefore the current growth of crops, supported that the chemical is suggested that isn't suitable for the important time analysis.

Proposed Work

This work focuses in work the prediction of Crop yield and also the price estimation. The planned methodology uses the tree algorithmic program so as to predict the results expeditiously and proves to best appropriate for the research work. the information collected, is analysed and worked to predict the yield and also the price of the crops at any given time.
The analysis work majorly involves the subsequent implementation modules.
1. Data Acquisition
2. Data Exploration
3. Machine learning prediction
4.Web application

Dataset is ready by aggregation the crop information obtained from the general public repository. There ar a couple of datasets that contain information. we tend to obtained the information that contains the main points of the downfall of the individual
crops.
A sample of non inheritable set of information and their attribute ar shown within the figure four.2 below, where WPI is represented as Wholesale Price index.


Figure 4.2 Dataset

Module 2: Data Exploration

Exploratory information analysis (EDA) is a necessary advance that happens once element developing with and obtaining data and it ought to be done before any demonstrating. this could get on the grounds that it's essential for Associate in Nursing data investigator really to nearly comprehend the thought of the information
while not making suspicions. The once impact of data investigation ar usually really helpful in getting a handle on the structure of the information, the appropriation of the qualities, and thus the space of
extraordinary qualities and interrelationships among the informational index.

The purpose of EDA is:
 To utilize outline measurements and representations to any or all or a ton of apparently comprehend information, discover things of information relating to the inclinations of the information, its quality and to detail suppositions and therefore the speculation of our hypothesis.
 For information pre-processing to be effective, it's basic to possess a general image of your information Basic factual portrayals van utilized to differentiate properties. Next step is to explore the knowledge. There sq. measure a pair of approaches wish to look at the knowledge using: Descriptive statistics is that the strategy toward gathering key attributes of the informational index into straightforward numeric measurements. a bit of the regular measurements utilized unit mean, variance, and relationship.

Visualization is that the strategy toward anticipating the information, or parts of it, into scientist space or into dynamic photos. among the information mining methodology, information investigation is employed throughout a giant choice of steps at the side of preprocessing, modelling, and interpretation of results.

During this method of study, Univariate and quantity analysis is done. 

Module 3: Machine learning Prediction

Machine learning prediction has these following steps:

1. Divide information into a pair of parts: training and testing data.
2. shaping the algorithmic programs particularly call tree algorithm.
3. coaching and testing against the algorithms.
4. change the programme with the calculated values.

Decision tree algorithm
Decision tree is degree formula that uses a tree like graph or model and their potential outcomes to predict the last word call, this formula uses conditional management statement. a decision tree is degree formula for approaching discrete-valued target functions, throughout that decision tree is denoted by a learned perform. For inductive learning these varieties of varieties of unit really notable and are successfully applied to a broad vary of tasks. we tend to tend to supply label to a greenhorn dealing that is whether or not or not it's legit or fraud that class label is unknown then dealing value is tested against the selection tree, and at that point from root node to output/class label for that dealing a path is derived. decision rule determines the results of the content of leaf node. Normally rules have the form of “If condition one and condition 2 but not condition 3 then outcome‟. decision tree helps to figure out the worst, best and expected values for numerous things, simplified to grasp and interpret and allow addition of latest potential things. Steps for making a decision tree unit of measurement that foremost to Calculate the entropy of every attribute exploitation the dataset in draw back then dataset is split into subsets exploitation the attribute that gain is most or entropy is minimum at that point to create a decision tree node containing that attribute and last rule is performed on subsets exploitation remaining attributes to make a call tree.

Results and Evaluation 

In the evaluation, we want to understand, for a number of metrics, whether our method works well for the 
problem statement we are trying tackle. We calculate the crop yield, its increase or decrease and also its price. 

Figure 5.1 shows the top gaining crops obtained using Decision tree algorithm.These are the crops that have had a considerable increase in their yield and the weather and soil conditions favour their production .Hence on logging in to our web application and subsequently clicking on the top gainers section will show the constant fluctuation in the prices and changes occurring minute by minute hence making the concerned user aware of the trends and help him/her make an informed decision based on most recent statistics.


Figure 5.1 -Top 5 gaining crops

Figure 5.2 represents those crops which are going downhill in the production market and also that it isn’t wise to go spending your money and time in sowing these crops as the algorithm from all the data has assessed that the below mentioned crops are not giving the desired yield hence directly effecting their market value so it would be considered wise to avoid them or plan the sowing likewise.

Figure 4.5 lowest yield crops


Figure 5.3 represents all the crops explored in the study I.e. all the crops whose data is available to us and we have shortlisted for our assessment from the government website.

		Figure 5.3 Kharif/Rabi crops 
