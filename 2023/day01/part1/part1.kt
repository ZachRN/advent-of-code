import java.io.File
import java.io.InputStream
//Advent of Code Day 1 Part 1 - @ZachRN Github

//Val can't be reassigned, but var can be good to know.
//First time ever writing Kotlin, much knowledge acquired, very wow
fun main()
{
	val inputStream: InputStream = File("input.txt").inputStream();
	var lineList = mutableListOf<String>();
	var total = 0;
	
	inputStream.bufferedReader().forEachLine { lineList.add(it) };
	lineList.forEach{
		var parsed = it.filter { it.isDigit() };
		val result = parsed[0].digitToInt() * 10 + parsed[parsed.length - 1].digitToInt()
		total += result;
	}
	println(total);
}