using System;
using System.Collections.Generic;
using System.ComponentModel.DataAnnotations;
using System.Linq;
using System.Web;

namespace Reports_Manager.Models
{
    public class Report
    {
        [Key]
        public int Id { get; set; }
        [Required]
        public int User_id { get; set; }
        [Required]
        public string Shop_id { get; set; }
        public string Serie { get; set; }
        public int Categoriy_id { get; set; }
        public DateTime Created_at { get; set; }
        public DateTime Updated_at { get; set; }
        public string Asked_by { get; set; }
        public string Notes { get; set; }
        public TimeSpan T_spend { get; set; }
        public TimeSpan T_travel { get; set; }
        public TimeSpan T_plus { get; set; }
        public string Description { get; set; }
        public string Analysis { get; set; }
        public string Facts { get; set; }
        public string Forecast { get; set; }

    }
}