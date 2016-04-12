import java.util.*;

public class JavaTest {
    public static void main(String[] args) {
        Random ran = new Random();

        for (int i = 0; i < 50; i++) {
            System.out.println(ran.nextInt(6) + 1);
        }
    }
}
