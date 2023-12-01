import java.io.File
import java.io.InputStream


//Val can't be reassigned, but var can be good to know.
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