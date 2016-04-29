﻿
using Reports_Manager.Properties;
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
        public DateTime? Date_sm { get; set; }
        public DateTime? Date_fact { get; set; }

        public virtual Article Article { get; set; }
        public virtual List<Report> Reports { get; set; }

        public Shop()
        {
            this.get_article();
        }

        public void get_article()
        {
            CarrierDataEntities database = new CarrierDataEntities();
            this.Article = database.Articles.First(article => article.Id == this.Article_id);
        }

        public void get_reports()
        {
            CarrierDataEntities database = new CarrierDataEntities();
            this.Reports = database.Reports.Where( report => report.Shop_otp == Otp).ToList() ;
        }

        public TimeSpan? time_spend()
        {
            TimeSpan? time_spend = TimeSpan.Parse("00:00:00");
            foreach( Report report in this.Reports)
            {
                if (report.T_spend != null)
                {
                    time_spend = time_spend + report.T_spend;
                }
                if (report.T_travel != null)
                {
                    time_spend = time_spend + report.T_travel;
                }
            }

            return time_spend ;
        }

        public string expense()
        {
            TimeSpan time_spend = (TimeSpan)this.time_spend();
            double total_cost = time_spend.TotalHours * Settings.Default.technic_cost_per_hour;
            return total_cost.ToString("0.00 €");
        }


        public string print_adress()
        {
            return @String.Format("{0}, {1}, {2}", Adresse, Code_postal, Ville);
        }

    }
}