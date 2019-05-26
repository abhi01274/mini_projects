

"""
Code Challenge
  Name: 
    Vocabulary
  Filename: 
    Vocabulary.py
  Problem Statement:
    Novel = james_joyce_ulysses.txt
    The claim is that James Joyce used in his novel more words than any other author. 
    Actually his vocabulary is above and beyond all other authors, 
    maybe even Shakespeare.
    
    1. Find the total number of words in the novel
    2. many words occur multiple time:["the", "while", "good", "bad", "ireland", "irish"]
    3. Quality of a novel is the number of different words.
       Find the number of different words used
    4. look at the other novels and find the total words and unique words for comparison
       novels = ['sons_and_lovers_lawrence.txt',
          'metamorphosis_kafka.txt',
          'the_way_of_all_flash_butler.txt',
          'robinson_crusoe_defoe.txt',
          'to_the_lighthouse_woolf.txt',
          'james_joyce_ulysses.txt',
          'moby_dick_melville.txt']

    5. Special Words in Ulysses novel by comparing with others, 
       words which are only used in Ulysses, store it in a file

    6. Common Words - Find the words which occur in every book.

  Hint: 
     Use Dictionary, Sets, Regex, File Handling
     re.findall(r"\b[\w-]+\b", ulysses_txt)
     

"""

