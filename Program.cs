using System;
//using System.Collections.Generic;
//using System.Linq;
//using System.Text;
//using System.Threading.Tasks;

namespace ebifredrick_first_C__project
{
    internal class Program
    {
        static void Main(string[] args)
        {
            Console.Write("Please type in your score (/100) to get your grade: ");
            int response = Convert.ToInt32(Console.ReadLine());
            Console.WriteLine("");
            if (response < 40)
            {
                Console.WriteLine("Sorry bro, chai");
            }
            else if (response > 40 & response < 45)
            {
                Console.WriteLine("E, na God save you o");
            }
            else if (response > 45 & response < 50)
            {
                Console.WriteLine("Sorry about this D");
            }
            else if (response > 50 & response < 60)
            {
                Console.WriteLine("C, it could have been worse");
            }
            else if (response > 60 & response < 70)
            {
                Console.WriteLine("B bro, it is a B, great!!");
            }
            else if (response > 70 & response < 101)
            {
                Console.WriteLine("A ooo, na A you get!!! Hurray!!");
            }
            else { Console.WriteLine("Which kind school give you this result?? Na for Benin Republic?"); }
        }
    }
}
