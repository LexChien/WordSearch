# WordSearch

## Usage
To use the WordSearch program, follow these steps:

1. Install the required dependencies by running the following command:
    ```
    pip install -r requirements.txt
    ```

2. Import the WordSearch module in your Python script:
    ```python
    from WordSearch import WordSearch
    ```

3. Create an instance of the WordSearch class:
    ```python
    word_search = WordSearch()
    ```

4. Use the `search` method to search for Chinese rare characters:
    ```python
    result = word_search.search("笠鳥")
    ```

    The `search` method returns the corresponding rare character for the input word.

5. Repeat step 4 for any other words you want to search.

6. Finally, don't forget to close the WordSearch instance when you're done:
    ```python
    word_search.close()
    ```

That's it! You can now easily search for Chinese rare characters using the WordSearch program.

## License

This program is licensed under the [MIT License](https://opensource.org/licenses/MIT).