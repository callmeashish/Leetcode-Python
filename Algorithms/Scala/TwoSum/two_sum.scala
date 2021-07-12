import scala.collection.mutable.Map

object Solution{

    def twoSum(nums: Array[Int], target: Int): Array[Int] = {

        val map = Map[Int,Int]();

        for (i <- 0 until  nums.length){
            val comp = target-nums(i)
            if(map.contains(comp)){
                return Array(map.get(comp).get,i)
            }
            map(nums(i)) = i
        }
        throw new IllegalArgumentException("No two sum solution")
    }

    def main(args: Array[String]) {
      println((twoSum( Array(2,7,11,15), 9)).mkString(", "));
    }
}