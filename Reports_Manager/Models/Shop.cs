using System;
using System.Collections.Generic;
using System.ComponentModel.DataAnnotations;
using System.Linq;
using System.Web;

namespace Reports_Manager.Models
{
    public class Shop
    {
        public int Article_id { get; set; }
        public int Serie { get; set; }
        [Key] public int Id { get; set;  }
        public int Adresse { get; set; }
        public int Code_postal { get; set; }
        public int Ville { get; set; }
        public int N_sortie { get; set; }
        public int Date_sm { get; set; }
        public int Date_fact { get; set; }

    }
}