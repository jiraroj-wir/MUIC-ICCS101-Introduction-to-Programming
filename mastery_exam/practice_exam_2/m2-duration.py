class Duration:
    def __init__(self, hours=0, days: int = 0, weeks: int = 0) -> None:
        self.hours = hours
        self.days = days
        self.weeks = weeks

    def extendBy(self, hr: int) -> None:
        self.hours += hr

        if self.hours >= 24:
            temp = self.hours // 24
            self.hours %= 24
            self.days += temp

        if self.days >= 7:
            temp = self.days // 7
            self.days %= 7
            self.weeks += temp

    # the upper ones got lsp-warnings
    # let python figure 'other' type itself?
    # def isShorterThan(self, other: Duration) -> bool:
    def isShorterThan(self, other) -> bool:
        """
        if self.weeks < other.weeks:
            return True
        elif self.weeks > other.weeks:
            return False
        else:
            if self.days < other.days:
                return True
            elif self.days > other.days:
                return False
            else:
                if self.hours < other.hours:
                    return True

                return False
        """

        duration = [self, other]
        sorted_duration = sorted(
            duration, key=lambda d: (d.weeks, d.days, d.hours), reverse=False
        )

        return (not (sorted_duration[0] == sorted_duration[1])) and (
            sorted_duration[0] == self
        )


### duration ###
eoyfmln = Duration()
qdrycoi = Duration()
bvugkhj = Duration()
eoyfmln.extendBy(145)
assert eoyfmln.weeks == 0 and eoyfmln.days == 6 and eoyfmln.hours == 1
assert eoyfmln.isShorterThan(eoyfmln) == False
qdrycoi.extendBy(642)
assert qdrycoi.weeks == 3 and qdrycoi.days == 5 and qdrycoi.hours == 18
assert qdrycoi.isShorterThan(qdrycoi) == False
eoyfmln.extendBy(980)
assert eoyfmln.weeks == 6 and eoyfmln.days == 4 and eoyfmln.hours == 21
assert qdrycoi.isShorterThan(eoyfmln) == True
qdrycoi.extendBy(165)
assert qdrycoi.weeks == 4 and qdrycoi.days == 5 and qdrycoi.hours == 15
assert qdrycoi.isShorterThan(qdrycoi) == False
bvugkhj.extendBy(185)
assert bvugkhj.weeks == 1 and bvugkhj.days == 0 and bvugkhj.hours == 17
assert eoyfmln.isShorterThan(bvugkhj) == False
qdrycoi.extendBy(793)
assert qdrycoi.weeks == 9 and qdrycoi.days == 3 and qdrycoi.hours == 16
assert qdrycoi.isShorterThan(eoyfmln) == False
eoyfmln.extendBy(172)
assert eoyfmln.weeks == 7 and eoyfmln.days == 5 and eoyfmln.hours == 1
assert eoyfmln.isShorterThan(eoyfmln) == False
bvugkhj.extendBy(994)
assert bvugkhj.weeks == 7 and bvugkhj.days == 0 and bvugkhj.hours == 3
assert eoyfmln.isShorterThan(bvugkhj) == False
bvugkhj.extendBy(130)
assert bvugkhj.weeks == 7 and bvugkhj.days == 5 and bvugkhj.hours == 13
assert bvugkhj.isShorterThan(qdrycoi) == True
eoyfmln.extendBy(254)
assert eoyfmln.weeks == 9 and eoyfmln.days == 1 and eoyfmln.hours == 15
assert eoyfmln.isShorterThan(bvugkhj) == False
bvugkhj.extendBy(297)
assert bvugkhj.weeks == 9 and bvugkhj.days == 3 and bvugkhj.hours == 22
assert bvugkhj.isShorterThan(bvugkhj) == False
qdrycoi.extendBy(699)
assert qdrycoi.weeks == 13 and qdrycoi.days == 4 and qdrycoi.hours == 19
assert bvugkhj.isShorterThan(qdrycoi) == True
qdrycoi.extendBy(412)
assert qdrycoi.weeks == 16 and qdrycoi.days == 0 and qdrycoi.hours == 23
assert qdrycoi.isShorterThan(qdrycoi) == False
eoyfmln.extendBy(668)
assert eoyfmln.weeks == 13 and eoyfmln.days == 1 and eoyfmln.hours == 11
assert qdrycoi.isShorterThan(eoyfmln) == False
eoyfmln.extendBy(732)
assert eoyfmln.weeks == 17 and eoyfmln.days == 3 and eoyfmln.hours == 23
assert bvugkhj.isShorterThan(eoyfmln) == True
