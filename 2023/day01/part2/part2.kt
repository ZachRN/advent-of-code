import java.io.File
import java.io.InputStream

//Advent of Code Day 1 Part 2 - @ZachRN Github

fun convertTextToNumber(text: String): String
{
	val lowerCaseText = text.lowercase()

	return when (lowerCaseText)
	{
		"one" -> return ("1")
        "two" -> return ("2")
        "three" -> return ("3")
		"four" -> return ("4")
		"five" -> return ("5")
		"six" -> return ("6")
		"seven" -> return ("7")
		"eight" -> return ("8")
		"nine" -> return ("9")
		"zero" -> return ("0")
		else -> return (text)
	}
}

fun main()
{
	val inputStream: InputStream = File("input.txt").inputStream();
	var lineList = mutableListOf<String>();
	var total = 0;

	inputStream.bufferedReader().forEachLine { lineList.add(it) };
	val keyWords = arrayOf("one", "two", "three", "four", "five", "six", "seven", "eight", "nine", "1", "2", "3", "4", "5", "6", "7", "8", "9", "0");
	lineList.forEach{
		val curLine = it;
		val map = mutableMapOf<Int, String>();
		for (i in 0..curLine.length)
		{	
			for (key in keyWords)
			{
				if (curLine.indexOf(key, i) != -1)
					map.put(curLine.indexOf(key, i), key)
			}
		}
		val sortedMap = map.toSortedMap()
		val firstKeyValue: String? = convertTextToNumber(sortedMap[sortedMap.firstKey()]!!);
		val lastKeyValue: String? = convertTextToNumber(sortedMap[sortedMap.lastKey()]!!);
		if (firstKeyValue != null && lastKeyValue != null)
		{
			val result = firstKeyValue.toInt() * 10 + lastKeyValue.toInt();
			total += result;
		}
	}
	println(total);
}