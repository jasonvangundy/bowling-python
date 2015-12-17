class Game:
    def __init__(self):
        self.frames = [Frame(1)]

    def roll(self, val):
        most_recent_frame = self.frames.pop()
        self.frames.append(most_recent_frame)
        if most_recent_frame.is_complete():
            frame = Frame(len(self.frames) + 1)
            frame.first_roll(val)
            self.frames.append(frame)
        else:
            if most_recent_frame.roll1_complete:
                most_recent_frame.second_roll(val)
            else:
                most_recent_frame.first_roll(val)

    def build_score(self, frames=None, total=None):
        if total is None:
            total = 0

        if frames is None:
            frames = self.frames

        if 0 == len(frames):
            return total

        frame_total = 0
        current_frame = frames[0]
        next_frame = Frame(0) if len(frames) == 1 else frames[1]
        frame_total += current_frame.sum()
        if current_frame.spare() or current_frame.strike():
            frame_total += next_frame.roll1

        if current_frame.strike():
            frame_total += next_frame.roll2
            if next_frame.strike() and len(frames) > 2:
                frame_total += frames[2].roll1

        total += frame_total
        if 10 == current_frame.frame_number:
            return total
        else:
            return self.build_score(frames=frames[1:], total=total)


class Frame:
    def __init__(self, frame_number):
        self.roll1 = 0
        self.roll1_complete = False
        self.roll2 = 0
        self.roll2_complete = False
        self.frame_number = frame_number

    def first_roll(self, val):
        self.roll1 = val
        if self.strike():
            self.roll2_complete = True

        self.roll1_complete = True

    def second_roll(self, val):
        self.roll2 = val
        self.roll2_complete = True

    def is_complete(self):
        return self.roll1_complete and self.roll2_complete

    def strike(self):
        return self.roll1 == 10

    def spare(self):
        return self.roll1 < 10 and (self.roll1 + self.roll2 == 10)

    def sum(self):
        return self.roll1 + self.roll2

    def is_final_frame(self):
        return self.frame_number > 10 and not self.strike()
