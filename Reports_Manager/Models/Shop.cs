using System;
using System.Collections.Generic;
using System.ComponentModel.DataAnnotations;
using System.Linq;
using System.Web;

namespace Reports_Manager.Models
{
    public class Shop
    {
        [Key]
        public int Id { get; set; }
        public string Article_id { get; set; }
        public string Serie { get; set; }
        public string Otp { get; set;  }
        public string Magasin { get; set; }
        public string Adresse { get; set; }
        public string Code_postal { get; set; }
        public string Ville { get; set; }
        public int N_sortie { get; set; }
        public DateTime Date_sm { get; set; }
        public DateTime Date_fact { get; set; }


    }
}