namespace Reports_Manager.Models
{
    using System;
    using System.Data.Entity;
    using System.ComponentModel.DataAnnotations.Schema;
    using System.Linq;

    public partial class User : DbContext
    {
        public User()
            : base("name=Carrier_data_connexion")
        {
        }

        public virtual DbSet<users> users { get; set; }

        protected override void OnModelCreating(DbModelBuilder modelBuilder)
        {
            modelBuilder.Entity<users>()
                .Property(e => e.firstname)
                .IsFixedLength();

            modelBuilder.Entity<users>()
                .Property(e => e.lastname)
                .IsFixedLength();
        }
    }
}
