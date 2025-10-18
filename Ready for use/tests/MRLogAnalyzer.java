import java.io.BufferedReader;
import java.io.FileReader;
import java.io.IOException;
import java.util.HashMap;
import java.util.Map;

public class MRLogAnalyzer {
    public static void main(String[] args) {
        String logFile = "C:\\Users\\Administrator\\Desktop\\kill result2.txt"; // 修改为你的日志文件路径
        Map<String, int[]> mrStats = new HashMap<>();

        try (BufferedReader br = new BufferedReader(new FileReader(logFile))) {
            String line;
            while ((line = br.readLine()) != null) {
                line = line.trim();
                if (!line.matches("\\[MR[\\w_]+\\] (KILLED|SURVIVED)")) continue;

                String[] parts = line.split("]");
                String mrName = parts[0].substring(1);  // 去掉 [
                String result = parts[1].trim();

                mrStats.putIfAbsent(mrName, new int[2]); // [0] = KILLED, [1] = SURVIVED
                if (result.equals("KILLED")) {
                    mrStats.get(mrName)[0]++;
                } else {
                    mrStats.get(mrName)[1]++;
                }
            }

            System.out.println("MR杀死率统计结果：");
            for (Map.Entry<String, int[]> entry : mrStats.entrySet()) {
                String mr = entry.getKey();
                int killed = entry.getValue()[0];
                int survived = entry.getValue()[1];
                int total = killed + survived;
                double killRate = total == 0 ? 0 : (double) killed / total;
                System.out.printf("%-10s : KILLED=%-4d SURVIVED=%-4d  KillRate=%.2f%%%n",
                        mr, killed, survived, killRate * 100);
            }

        } catch (IOException e) {
            System.err.println("读取日志文件时出错: " + e.getMessage());
        }
    }
}
