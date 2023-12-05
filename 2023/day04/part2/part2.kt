import java.io.File
import java.io.InputStream

fun main()
{
	val inputStream: InputStream = File("input.txt").inputStream();
	var lineList = mutableListOf<String>();

	inputStream.bufferedReader().forEachLine { lineList.add(it) };
	var scratchArray = IntArray(lineList.size) { 1 }
	for (x in 0..lineList.size - 1)
	{
		var scratchModifier = 1;

		var stringHold = lineList[x].toString();
		stringHold = stringHold.drop(stringHold.indexOf(":") + 2);

		//Scuffed Parsing
		var splitPart = stringHold.split("|");
		var firstHalf = splitPart[0].trim().split("\\s+".toRegex());
		var secondHalf = splitPart[1].trim().split("\\s+".toRegex());
		for (item in secondHalf)
		{
			// println(item)
			if (item in firstHalf)
			{
				scratchArray[x + scratchModifier] += scratchArray[x];
				scratchModifier++;
			}
		}
	}
	println(scratchArray.sum())
}