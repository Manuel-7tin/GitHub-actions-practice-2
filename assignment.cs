using System;
using System.Collections.Generic;

/// <summary>
/// A generic sorting utility class for sorting lists of type T.
/// </summary>
public static class Sorter<T>
{
    /// <summary>
    /// Sorts the given list in ascending or descending order using the specified comparer.
    /// </summary>
    /// <typeparam name="T">The type of elements in the list.</typeparam>
    /// <param name="list">The list to be sorted. This list is modified in place.</param>
    /// <param name="comparer">An optional comparer for custom sorting. If null, default comparer is used.</param>
    /// <param name="descending">If true, sorts the list in descending order; otherwise, ascending.</param>
    public static void Sort<T>(List<T> list, IComparer<T> comparer = null, bool descending = false)
    {
        if (list == null) throw new ArgumentNullException(nameof(list));

        comparer ??= Comparer<T>.Default;

        list.Sort((x, y) => descending
            ? comparer.Compare(y, x)
            : comparer.Compare(x, y));
    }
}

public class Assignment
{
    public static void Main(string[] args)
    {
        List<int> numbers = new List<int> { 5, 2, 9, 1, 3 };
        Sorter<int>.Sort(numbers);  // Ascending
        foreach (var number in numbers)
        {
            Console.WriteLine(number);
        }
        
        List<string> names = new List<string> { "Zoe", "Anna", "Mike" };
        Sorter<string>.Sort(names, descending: true);  // Descending
        foreach (var name in names)
        {
            Console.WriteLine(name);
        }
    }
}
