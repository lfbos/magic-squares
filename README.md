# magic-squares
Script that shows how a magic square is constructed from an odd integer

## Magic Square
A magic square is a square grid of distinct numbers such that each row and column add
up to the same number. Further, the two diagonals (from corner to corner) also add up to
that number. For more information: [Wikipedia](https://en.wikipedia.org/wiki/Magic_square#Types_of_construction)

## Run the script

* Clone the project

    `git clone https://github.com/lfbos/magic-squares.git`

* Enter into the project

    `cd magic-squares`

* Create python environment

    * Virtualenvwrapper: using [virtualenvwrapper](https://virtualenvwrapper.readthedocs.io/en/latest/):

        ```
        mkvirtualenv env_name --python=python3
        pip install -r requirements.txt
        ```

    * Virtualenv: using [virtualenv](https://virtualenv.pypa.io/en/stable/):

        ```
        virtualenv env
        source env/bin/activate
        pip install -r requirements.txt
        ```

* Run the script `python magic_squares.py`
