from src import hops


class HopsCollection:
    repository: HopsRepository

    def add_hops(hops: hops.Hops) -> None:
        # check if hops already exists

        # if not, add it to the database
        if not self.repository.exists(hops):
            self.repository.add(hops)
        else:
            raise HopsAlreadyExistsException
