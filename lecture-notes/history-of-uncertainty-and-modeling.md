# History of Uncertainty and Computational Modeling

## Uncertainty
  * As a species, we’ve been exposed to uncertainty, both actively and passively, throughout our existence.
    * Passively, through weather, disease, and natural catastrophes
    * Actively, through games of chance
  * Some of these processes, e.g., chance of precipitation, are “more random” than others, e.g., procession of tides.
  * (We could characterize degree of randomness through the concept of entropy)
  * For most of human history, we have rationalized away uncertainty as deterministic, outcomes representing the will of spiritual/religious forces.
  * The earliest forms of predictions reflected this model of uncertainty:
    * Hepatoscopy of the Mesopotamians
    * Augury of the Greek, Etruscans, and Romans
    * Animal behavior of various Native American tribes
    * Astrology of nearly all cultures
  * Thanks largely to profligate gamblers and their interactions with natural philosophers, we slowly began to systematize game of chance.
    * Cardano, Liber de ludo aleae, 1564
    * Huygens,  De Ratiociniis in Ludo Aleae, 1657
    * de Moivre, The Doctrine of Chances, 1718
    * Hoyle, A Short Treatise on the Game of Whist, 1743
    * Fra Luca, Tartaglia, Fermat, and Pascal, famously on the problem of points
  * Increasingly, some also began to analogize these ideas into domains outside of games of chance:
    * Arnauld, La logique ou l'art de penser, 1662
    * Graunt, Natural and Political Observations Made upon the Bills of Mortality, 1662
    * Leibniz, De Arte Combinatoria, 1666
    * Jacob Bernoulli, Ars Conjectandi, 1689
    * Buffon’s needle experiment, 1777
    * Laplace: Théorie analytique des probabilités, 1812
  * In the period after Laplace’s treatise and until the early 20th century, little changed within the paradigm of probability.
  * However, prior to Laplace, probability had a more nuanced conception than after.
    * Many “probabilities” are epistemic, not aleatory, in that they don’t correspond to long-run proportions or propensities.
    * When you consider a statement like “Candidate X will be elected President” (A), you retrieve a body of evidence.  Based on this body of evidence, you might assign a probability between 0 and 1 to the event.
    * However, when you consider complementary event, “Candidate X will not be elected President” (¬A), the body of evidence you retrieve for reasoning may not be identical.  
  * In the late 19th and early 20th century, we took the next great step -  the development of statistics as a science.
    * Many of our earlier protagonists like Bernoulli, de Moivre, and Laplace investigated the properties of samples and related claims.
	* However, statistics as a science required the internalization of a new question - what is the probability of a probability?
	* This second-order abstraction was not novel, dating back to problems of "inverse probability" as addressed by those like Bayes.
	* The protagonists of this story are names you are likely more familiar with: Gosset ("Student"), Fisher, Neyman, and Pearson
	* Their developments and disagreements led to the hypothesis testing framework we use so heavily today, as well as substantial growth in the application of statistical methods to new disciplines.

## Computing
  * The history of computing begins long before the 20th century, but we'll start here.
  * Contemporaneously, two World Wars led to substantial investment not just in decision science, but also in physics and computing.
    * During the war, analysts relied on millions of computations to manage war efforts and develop new weapons
	* The majority of these computations were performed by Computers - armies of humans, typically female, who were organic arithmetic engines
	* However, a new kind of computer - less organic - was entering the picture.
  * In arguably the greatest confluence of genius our species has experienced, the Manhattan Project and subsequent nuclear weapon projects bring together figures like Stan Ulam and John von Neumann.
    * The group had been attacking a number of problems around neutron multiplication in fission weapons.  However, the resulting differential equations and integrals were intractable.
	* Ulam, sick in bed playing solitaire, however, has an idea - instead of calculating probabilities of hands using combinatorics, what about averaging hundreds of plays?
	* Realizing the applications to integration and many problems in mathematical physics, he communicates the idea to von Neumann.
	* von Neumann and Ulam, both deeply interested in the recent development of digital computing, decide to attack the neutron diffusion problem on the brand new ENIAC computer.
	* The rest is history - for ENIAC, Monte Carlo, and the hydrogen bomb.
  * However, Monte Carlo needs more than just digital computing; it also needs "random" numbers
    * Our human Computer war heros had a source - printed tables, often derived from real gambling devices like roulette wheels
	* Rand Corp, responding to the growth of Monte Carlo and need for random numbers, publishes a real thriller - A MILLION Random Digits WITH 100,000 Normal Deviates
	* In the process, Rand and others develop new methods for generating and assessing pseuodrandom numbers on computers
  * And so the groundwork has been laid for humans to explore uncertainty through computational modeling, applying probability and statistics to models executed on digital computers


### Links/Resources
  * http://www.informs-sim.org/wsc09papers/028.pdf
  * http://www.ise.ncsu.edu/jwilson/simhist10.pdf
  * http://www.lancaster.ac.uk/pg/jamest/Group/intro2.html
  * http://www.cs.fsu.edu/~mascagni/MC_Basics.pdf
  * http://www.landersimulation.com/eng/training-with-simulation/the-world-in-motion/history-of-simulation/
  * https://www.researchgate.net/publication/221526570_A_brief_history_of_simulation_revisited
  * http://library.lanl.gov/cgi-bin/getfile?00326867.pdf
  * http://www.ncbi.nlm.nih.gov/pmc/articles/PMC2924739/
  * https://en.wikipedia.org/wiki/Monte_Carlo_method#History
  * https://en.wikipedia.org/wiki/Timeline_of_scientific_computing
  * https://en.wikipedia.org/wiki/Augury
  * https://en.wikipedia.org/wiki/Omen
  * http://arxiv.org/pdf/0808.2902.pdf
  * https://www.cs.xu.edu/math/Sources/JakobBernoulli/jakob%20and%20leibniz.pdf
  * https://www.maa.org/sites/default/files/pdf/upload_library/22/Allendoerfer/stahl96.pdf
  * https://www.rand.org/content/dam/rand/pubs/monograph_reports/MR1418/MR1418.deviates.pdf
  * http://www.amazon.com/Willful-Ignorance-The-Mismeasure-Uncertainty/dp/0470890444
  * http://www.amazon.com/Probability-Philosophical-Introduction-D-H-Mellor/dp/0415282500/ref=mt_hardcover?_encoding=UTF8&me=
  * http://www.amazon.com/The-Emergence-Probability-Philosophical-Probabilistic/dp/0521685575
  
