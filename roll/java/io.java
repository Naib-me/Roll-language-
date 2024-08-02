    /**
     * io
     */
    public class io {
        public static void print(Object text) {
            // 检查是否为null
            if (text == null) {
                System.out.print("null");
            } else {
                // 使用toString()方法将对象转换为字符串
                System.out.print(text.toString());
            }
        }

        public static void println(Object text) {
            // 检查是否为null
            if (text == null) {
                System.out.print("null");
            } else {
                // 使用toString()方法将对象转换为字符串
                System.out.println(text.toString());
            }
        }

        public static void newLine() {
            System.out.println();
        }
    }