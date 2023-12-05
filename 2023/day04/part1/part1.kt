import java.io.File
import java.io.InputStream

fun main()
{
	val inputStream: InputStream = File("input.txt").inputStream();
	var lineList = mutableListOf<String>();
	var total: Int = 0;

	inputStream.bufferedReader().forEachLine { lineList.add(it) };
	lineList.forEach{
		var toAdd = 0;

		var stringHold = it.toString();
		stringHold = stringHold.drop(stringHold.indexOf(":") + 2);

		//Scuffed Parsing
		var splitPart = stringHold.split("|");
		var firstHalf = splitPart[0].trim().split("\\s+".toRegex());
		var secondHalf = splitPart[1].trim().split("\\s+".toRegex());
		// println(firstHalf);
		// println(secondHalf);
		for (item in secondHalf)
		{
			// println(item)
			if (item in firstHalf)
			{
				// println("Got here!");
				if (toAdd == 0)
					toAdd = 1;
				else
					toAdd *= 2;
			}
		}
		total += toAdd
		// println(stringHold);
	}
	println(total)
}