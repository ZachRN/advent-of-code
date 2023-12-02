import java.io.File
import java.io.InputStream

fun main()
{
	val inputStream: InputStream = File("input.txt").inputStream();
	var lineList = mutableListOf<String>();

	val redMax: Int = 12;
	val greenMax: Int = 13;
	val blueMax: Int = 14;
	var sumTotal: Int = 0;

	inputStream.bufferedReader().forEachLine { lineList.add(it) };
	lineList.forEach{
		val gamePart = it.split(":");
		val gameInfo = gamePart[0].split(" ");
		val differentPulls = gamePart[1].split(";");
		val result = run { //Runs are weird.. so far..
			for (i in  0..differentPulls.size - 1)
			{
				val cubeSeperated = differentPulls[i].split(",");
				for (j in 0..cubeSeperated.size - 1)
				{
					val numColor = cubeSeperated[j].split(" ");
					if (numColor[1].toInt() > redMax && numColor[2] == "red")
						return@run false;
					if (numColor[1].toInt() > greenMax && numColor[2] == "green")
						return@run false;
					if (numColor[1].toInt() > blueMax && numColor[2] == "blue")
						return@run false;
				}
			}
			return@run true;
		}
		if (result == true)
			sumTotal += gameInfo[1].toInt();
	}
	println(sumTotal);

}