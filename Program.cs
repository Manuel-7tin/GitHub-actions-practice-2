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


using System;
using System.Collections.Generic;

public class Storage<T>
{
    private Dictionary<int, T> _items = new Dictionary<int, T>();

    public void Add(int id, T item)
    {
        _items[id] = item;
    }

    public T Get(int id)
    {
        if (_items.TryGetValue(id, out T value))
        {
            return value;
        }

        throw new KeyNotFoundException($"Item with ID {id} not found.");
    }

    public void PrintAll()
    {
        foreach (var pair in _items)
        {
            Console.WriteLine($"ID: {pair.Key}, Item: {pair.Value}");
        }
    }
}

public class Product
{
    public string Name { get; set; }
    public decimal Price { get; set; }

    public override string ToString()
    {
        return $"{Name} (${Price})";
    }
}

public class Program
{
    public static void Main()
    {
        // Example 1: Storage with string
        var stringStorage = new Storage<string>();
        stringStorage.Add(1, "Apple");
        stringStorage.Add(2, "Banana");

        Console.WriteLine(stringStorage.Get(1));  // Output: Apple
        stringStorage.PrintAll();

        Console.WriteLine();

        // Example 2: Storage with Product
        var productStorage = new Storage<Product>();
        productStorage.Add(101, new Product { Name = "Laptop", Price = 999.99m });
        productStorage.Add(102, new Product { Name = "Phone", Price = 499.50m });

        var p = productStorage.Get(101);
        Console.WriteLine(p);  // Output: Laptop ($999.99)
        productStorage.PrintAll();
        
        var warped = new Storage<Storage<string>>();
        warped.Add(1, stringStorage);
        warped.PrintAll();
        
    }
}
