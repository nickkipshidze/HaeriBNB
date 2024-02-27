# HaeriBNB

Georgian version of popular web service - AirBNB

**Goal:** Remake this website -> [www.airbnb.com](https://www.airbnb.com/)

## Running the code

1. Clone the repository:
    ```shell
    $ git clone https://github.com/NickKipshidze/HaeriBNB
    ````

0. Change into the repository directory (obviously):
    ```shell
    $ cd ./HaeriBNB
    ```

0. Start the backend:
    ```shell
    $ ./start.sh backend
    ```

0. Start the frontend:
    ```shell
    $ ./start.sh frontend
    ```

## Utility program (start.sh)

`start.sh` was written by me to help with managing and starting backend/frontend servers.

Very useful for cleaning cache and managing dependencies.

It just makes life easier. Try it.

### install

`install` command installs all python and npm packages/libraries.

```shell
$ ./start.sh install
```

### cleanup

`cleanup` command basically removes all cache directories.

```shell
$ ./start.sh cleanup
```

### count

`count` command just counts all lines of code. This one is mainly for me. (:

```shell
$ ./start.sh count
```