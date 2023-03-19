## For query classification: How many unique categories did you see in your rolled up training data when you set the minimum number of queries per category to 1000? To 10000?

For 1000 -> 374
For 10000 -> 58


## For query classification: What were the best values you achieved for R@1, R@3, and R@5? You should have tried at least a few different models, varying the minimum number of queries per category, as well as trying different fastText parameters or query normalization. Report at least 2 of your runs.

Default parameters
R@1     0.476, R@3     0.635, R@5     0.696

-lr 0.6 -epoch 19 -wordNgrams 2
R@1     0.524, R@3     0.708, R@5     0.771


## For integrating query classification with search: Give 2 or 3 examples of queries where you saw a dramatic positive change in the results because of filtering. Make sure to include the classifier output for those queries.

`memory -> pcmcat225800050009`
Without a classifier, also matched devices like `... X GB Memory`. With the classifier only returned memory cards.

`galaxy -> pcmcat209400050001` 
Without a classifier, the result set had screen protectors on the first and third positions, and a tablet on the second (okay, tablet wasn't bad). With the classifier all of the results became phones.

`playstation -> abcat0715007`
Without a classifier, only the second result was a console. The rest were primarily games and a couple of network cards. With the classifier they all became accesories - headphones, controllers, chargers and cables. Not exactly, what was expected, but still better than random games for PS.


## For integrating query classification with search: Give 2 or 3 examples of queries where filtering hurt the results, either because the classifier was wrong or for some other reason. Again, include the classifier output for those queries.

`toshiba -> pcmcat247400050000`
With classifier, it only returned laptops. Without, also had TVs, DVD players and portable HDDs.

`office -> abcat0508009`
With the classifier started only matching `Microsoft Office` products. Without it had surge protectors and ink cartridges.