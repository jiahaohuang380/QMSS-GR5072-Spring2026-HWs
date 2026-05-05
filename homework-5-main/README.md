## Instructions

-   Answer the questions below
-   Your final document should be an `.ipynb` file. You will submit this file, along with any other scripts (except for the module for question 6 which might have your API authentication details) you used to create the report, on Canvas.

### Assignment items `[100 pts]`

**Part 1:** Leverage the lecture code to answer these questions.

1.  [`10 pts`] Use the BLS Data Finder 1.1 available [here](https://data.bls.gov/dataQuery/search) to import a BLS variable/field (using the BLS web API) of your choosing.
2.  [`10 pts`] Using the BLS web API, create your own custom function which can interact with the BLS web API. Your function should take three input parameters: *name base_url_in*, *series_in*, and *title_in* and return the relevant data series as a `pd.DataFrame` object. Test your function by replicating the `GET` request you sent above for #1.
3.  [`10 pts`] Go to these three links: [link1](https://data.bls.gov/dataViewer/view/timeseries/APU0000709112), [link2](https://data.bls.gov/dataViewer/view/timeseries/APU000074714), [link3](https://data.bls.gov/dataViewer/view/timeseries/APU0000708111). On these webpages, you will see three different time series data sets. For each, you will also see both a Series Title and ID. Using the function you wrote to fetch data from the BLS web API, import these data sets into Python as three separate `pd.Data.Frame` objects.
4.  [`10 pts`] Merge the data sets together into a single `pd.DataFrame` and make a time series plot showing how the CPI for these three goods has changed over the last 24 months. Each good should be shown as a unique line with different coloring/patterns and a matching legend (I suggest using the `matplotlib` library to do this).
5.  [`10 pts`] In the lecture notes, refer to the section entitled "No Python Package? Manipulate URL directly". Can you update the code in the New York Times article search API URL so that you return article data for Hillary Clinton for the time range April 1, 2024 - April 4, 2024? How many TOTAL articles were returned by this API search?

**Part 2:** Connect to other APIs

6.  [`10 pts`] In this question, we will connect to the [Open Library API](https://openlibrary.org/developers/api). Open Library has a package called [openlibrary-client](https://github.com/internetarchive/openlibrary-client/tree/master) which makes this easy. Using their Python interface documentation, your task is to figure out how to use the authors function listed on this webpage to import [Christopher Moore](https://en.wikipedia.org/wiki/Christopher_Moore_(author))'s works. There is no API key required to use this package. Once you have successfully used openlibrary-client to pull in data for this author, write a for loop to display the following message, making sure you align the numbers as is done here:
 

    ![](images/openlibrary.png)

**Hints:** 1) The Christopher Moore you need to find was born in 1957.
 2) For more information, you can explore the function code here:
 https://github.com/internetarchive/openlibrary-client/blob/master/olclient/openlibrary.py
 or do help(ol.Author) in Python.
 3) String alignment was covered briefly in the JuPyter notebook on strings.

7.  [`10 pts`]  Do the same exercise with the Italian author [Gianrico Carofiglio](https://en.wikipedia.org/wiki/Gianrico_Carofiglio), a contemporary Italian crime writer.
 This time compare the results to a direct API query using the requests library in Python: https://openlibrary.org/search.json?author_key=INSERTKEY
 a) Which call returns more keys about each book? Why do you think that is? When would you choose one over the other?
 b) Loop over the results and print different messages based on the language of the book. If the book's language was Italian print "TITLE NAME was published in Italian". If it was published in English, print "TITLE NAME was published in English". (Make sure to include the actual title name and not TITLE NAME.)
 
Hint: Find the language key within the results to separate the loop into different conditions. 

8.  [`10 pts`] Find an API of interest to you. Sign up for an API key if necessary. Describe the API concisely and make a single call on the API and return an example of the returned data here.

**Part 3:** regex practice

9.  [`20 pts`] Import the data found in the HW5 folder. It is a single column of data that has 500 rows. This data represents a format of data that you will often encounter in research projects which use "thematic coding" for text response data. As described [here](https://www.betterevaluation.org/methods-approaches/methods/thematic-coding): "Thematic coding is a form of qualitative analysis that involves recording or identifying passages of text or images that are linked by a common theme or idea allowing you to index the text into categories and therefore establish a 'framework of thematic ideas about it' (Gibbs 2007)."

    It is ok if you are not familiar with thematic coding for qualitative/text data. Your task is to import the data and write a regex that is capable of finding the thematic code "1" whenever it appears in the string. This is more difficult than it sounds, because your regex should count all the "1"s that appear, but not "10", "11", "12", "21" etc. Also note, that sometimes "1" appears in the 2nd, 3rd... etc. position (e.g., "2, 6, 7, 1, 10"). Use this regex to add a new column to your dataset called "find_1". Display a frequency table showing the number of times your regex flagged "1" as appearing.
