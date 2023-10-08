import pandas
from bocfx import bocfx


class FX:
    def __init__(self, time):

        data = bocfx(FX='SGD', sort='SE,ASK', time=time)
        self.df = self.preprocess(data)

    def preprocess(self, data):

        df = pandas.DataFrame(data[1:], columns=(
            "FX", "ask", "time")).astype({"ask": float})
        df["time"] = pandas.to_datetime(df["time"])
        df["date"] = df["time"].dt.date

        return df

    def datemean(self):

        group = self.df.groupby("date")
        datemeantb = group["ask"].mean().round(2)

        return datemeantb

    def allmean(self):

        return self.datemean().mean().round(2)
