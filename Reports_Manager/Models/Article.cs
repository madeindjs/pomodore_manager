using System;
using System.Collections.Generic;
using System.ComponentModel.DataAnnotations;
using System.Linq;
using System.Web;

namespace Reports_Manager.Models
{
    public partial class Article
    {
        
        public string Id { get; set; }
        public string Designation { get; set; }
        public string Gamme { get; set; }
        public string Longueur { get; set;  }
        public string Usine { get; set; }
        [Key]
        public int Sql_id { get; set; }

        public virtual List<Shop> Shops { get; set; }

        public Article()
        {
            this.get_shops();
        }

        public void get_shops()
        {
            CarrierDataEntities database = new CarrierDataEntities();
            System.Data.Entity.DbSet<Shop> database_Shops = database.Shops;
            Shops = database_Shops.Where( shop => shop.Article_id == Id ).ToList() ;
        }

    }
}