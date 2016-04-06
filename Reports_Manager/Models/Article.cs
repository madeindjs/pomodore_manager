using System;
using System.Collections.Generic;
using System.ComponentModel.DataAnnotations;
using System.Linq;
using System.Web;

namespace Reports_Manager.Models
{
    public class Article
    {
        
        public string Id { get; set; }
        public string Designation { get; set; }
        public string Gamme { get; set; }
        public string Longueur { get; set;  }
        public string Usine { get; set; }
        [Key]
        public int Sql_id { get; set; }

    }
}