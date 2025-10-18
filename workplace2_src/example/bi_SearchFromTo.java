package example;

public class bi_SearchFromTo {//二分查找，查找key所在的位置

    public static int bi_SearchFromTo_m(Double[] elements, Double key, Integer from, Integer to) {
        int low = from;
        int high = to;
        while (low <= high) {
            int mid = (low + high) / 2;
            double midVal = elements[mid];
            if (midVal < key) {
                low = mid + 1;
            } else {
                if (midVal > key) {
                    high = mid - 1;
                } else {
                    return mid;
                }
            }
        }
        return -(low + 1);
    }
}