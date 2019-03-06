using System;

namespace Sandbox_1
{
    class Program
    {
        delegate int Function(int a, int b);
        static void Main(string[] args)
        {
            Console.WriteLine("Hello World!");

            Function func1 = (a, b) => a + b;
            Function func2 = (a, b) => a * b;

            Console.WriteLine(func1(5, 6));
            Console.WriteLine(func2(5, 6));

            Function func3 = (a, b) => { return a + 2 * b; };

            Console.WriteLine(func3(5, 6));
        }
    }
}
