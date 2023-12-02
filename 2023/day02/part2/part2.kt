import java.io.File
import java.io.InputStream

fun main()
{
	val inputStream: InputStream = File("input.txt").inputStream();
	var lineList = mutableListOf<String>();
	var sumTotal: Int = 0;

	inputStream.bufferedReader().forEachLine { lineList.add(it) };
	lineList.forEach{
		//Saving info for each cube and resetting it each line.
		var redNeeded: Int = 0;
		var greenNeeded: Int = 0;
		var blueNeeded: Int = 0;

		//Splitting the game info apart.
		val gamePart = it.split(":");
		val differentPulls = gamePart[1].split(";");
		//Unfortunatelty A Run isn't needed this time around :( there goes the learning
		for (i in  0..differentPulls.size - 1)
		{
			val cubeSeperated = differentPulls[i].split(",");
			for (j in 0..cubeSeperated.size - 1)
			{
				val numColor = cubeSeperated[j].split(" ");
				if (numColor[1].toInt() > redNeeded && numColor[2] == "red")
					redNeeded = numColor[1].toInt();
				if (numColor[1].toInt() > greenNeeded && numColor[2] == "green")
					greenNeeded = numColor[1].toInt();
				if (numColor[1].toInt() > blueNeeded && numColor[2] == "blue")
					blueNeeded = numColor[1].toInt();
			}
		}
		sumTotal += (redNeeded * greenNeeded * blueNeeded);
	}
	println(sumTotal);

}