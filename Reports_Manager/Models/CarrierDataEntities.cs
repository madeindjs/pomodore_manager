using System;
using System.Collections.Generic;
using System.Data.Entity;
using System.Linq;
using System.Web;

namespace Reports_Manager.Models
{
    public class CarrierDataEntities : DbContext
    {
        public DbSet<User> Users { get; set; }
    }
}