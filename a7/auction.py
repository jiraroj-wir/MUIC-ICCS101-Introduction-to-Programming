# Assignment 7, Task 4
# Name: Jiraroj Wiruchpongsanon
# Collaborators: <NAME_1, NAME_2>
# Time Spent: 1.5 hrs
# Use of AI: YES
# AI usage details: The instructions are so confusing for me, need a lot of explanation.
# Also, you need some kind of intuition to the whole problem first, before writing anythin


### Your code start here ######
class Bid:
    def __init__(self, bid_id, bidder_id, auction) -> None:
        self.bid_id = bid_id
        self.bidder_id = bidder_id
        self.auction = auction

    def __repr__(self) -> str:
        return f"{self.bid_id}, {self.bidder_id}, {self.auction}\n"

    def __str__(self) -> str:
        return f"bid: {self.bid_id} \t\t| bidder: {self.bidder_id} \t| auction: {self.auction}\n"

    def __lt__(self, other) -> bool:
        return self.bid_id < other.bid_id

    def __gt__(self, other) -> bool:
        return self.bid_id > other.bid_id

    def __le__(self, other) -> bool:
        return self.bid_id <= other.bid_id

    def __ge__(self, other) -> bool:
        return self.bid_id >= other.bid_id

    def __eq__(self, other) -> bool:
        return self.bid_id == other.bid_id


class Auction:
    def __init__(self, auction) -> None:
        self.auction = auction
        self.bids = []
        self.winner = None
        self.price = 1.0

    def placeBid(self, bidder_id) -> None:
        self.price += 1.5
        self.winner = bidder_id
        self.bids.append(bidder_id)

    def __repr__(self) -> str:
        return f"{self.winner}, {self.price}, {self.bids}\n"

    def __str__(self) -> str:
        return f"auction: {self.auction} \t| winner: {self.winner} \t| price: {self.price}\n"


# credit: https://www.geeksforgeeks.org/python/working-csv-files-python/
def CSV2List(csvFilename: str) -> list[Bid]:
    import csv

    bid_list = []
    with open(csvFilename, "r") as csvfile:
        # creating a csv reader object
        csvreader = csv.reader(csvfile)

        # extracting field names through first row
        fields = next(csvreader)
        if fields != ["bid_id", "bidder_id", "auction"]:
            raise ValueError(
                f"CSV header mismatch: Expected ['bid_id', 'bidder_id', 'auction'], but got {fields}"
            )

        # extracting each data row one by one
        for row in csvreader:
            bid = Bid(int(row[0]), row[1], row[2])
            bid_list.append(bid)

        # print("Total no. of rows: %d" % (csvreader.line_num))
        bid_list.sort(key=lambda b: b.bid_id)

    return bid_list


def mostPopularAuction(bidList: list[Bid]) -> set[str]:
    map = {}
    biggest_set = 0
    for bid in bidList:
        if bid.auction not in map:
            map[bid.auction] = set()

        map[bid.auction].add(bid.bidder_id)
        size = len(map[bid.auction])
        if size > biggest_set:
            biggest_set = size

    most_popular_auction = set()
    for key in map:
        if len(map[key]) == biggest_set:
            most_popular_auction.add(key)

    return most_popular_auction


def auctionWinners(bidList: list[Bid]) -> dict[str, Auction]:
    map = {}
    for bid in bidList:
        if bid.auction not in map:
            map[bid.auction] = Auction(bid.auction)

        map[bid.auction].placeBid(bid.bidder_id)

    return map
