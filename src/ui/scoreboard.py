class Scoreboard:
    """Class which handles the reading and writing of high scores to a text file

    Attributes:
        file_name: the name of the file in which the scores are stored
    """

    def __init__(self):
        """Constructor that sets the file name that is being used
        """

        self.file_name = "scoreboard.txt"

    def get_scores(self):
        """Reads the scores from the file and ensures the file contains scores for all three difficulties

        Returns:
            scores: list containing the high scores for all difficulties
        """

        scoreboard_file = self._open_file("r")
        scores = scoreboard_file.read().splitlines()
        scoreboard_file.close()
        if len(scores) != 3:
            scoreboard_file = self._create_file()
            scores = scoreboard_file.read().splitlines()
            scoreboard_file.close()
        for i in range(3):
            scores[i] = int(scores[i])
        return scores

    def add_score(self, difficulty, time):
        """Adds a new score to a file if it beats the current score stored for that difficulty

        Args:
            difficulty: integer value to show the difficulty at which the score was played
            time: the score that is being added, in milliseconds
        """
        scores = self.get_scores()
        if difficulty > 0 and difficulty < 4:
            previous_score = scores[difficulty-1]
            if previous_score < 0 or previous_score > time:
                scores[difficulty-1] = time

        scoreboard_file = self._open_file("w")
        scoreboard_file.write(str(scores[0]) + "\n" + str(scores[1]) + "\n" + str(scores[2]))
        scoreboard_file.close()

    def _open_file(self, mode):
        try:
            scoreboard_file = open(self.file_name, mode, encoding="utf8")
        except FileNotFoundError:
            scoreboard_file = self._create_file()
        return scoreboard_file

    def _create_file(self):
        new_file = open(self.file_name, "w", encoding="utf8")
        new_file.write("-1\n-1\n-1")
        new_file.close()
        scoreboard_file = open(self.file_name, "r", encoding="utf8")
        return scoreboard_file
