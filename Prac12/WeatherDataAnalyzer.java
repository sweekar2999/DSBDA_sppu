import java.io.*;

public class WeatherDataAnalyzer {
    public static void main(String[] args) throws IOException {
        String filename = "sample_weather.txt";

        BufferedReader reader = new BufferedReader(new FileReader(filename));

        String line;

        int count = 0;

        double totalTemperature = 0.0;
        double totalDewPoint = 0.0;
        double totalWindSpeed = 0.0;

        while ((line = reader.readLine()) != null) {
            String[] parts = line.split(",");

            if (parts.length >= 3) {
                totalTemperature += Double.parseDouble(parts[0]);
                totalDewPoint += Double.parseDouble(parts[1]);
                totalWindSpeed += Double.parseDouble(parts[2]);
                count++;
            }
        }

        if (count > 0) {
            double avgTemp = totalTemperature / count;
            double avgDew = totalDewPoint / count;
            double avgWind = totalWindSpeed / count;

            System.out.println("Average Temperature:" + avgTemp);
            System.out.println("Average DewPoint:" + avgDew);
            System.out.println("Average WindSpeed:" + avgWind);

        }
    }
}