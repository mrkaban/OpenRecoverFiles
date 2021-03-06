// Copyright (C) 2017  Joey Scarr, Josh Oosterman, Lukas Korsika
//
// This program is free software: you can redistribute it and/or modify
// it under the terms of the GNU General Public License as published by
// the Free Software Foundation, either version 3 of the License, or
// (at your option) any later version.
//
// This program is distributed in the hope that it will be useful,
// but WITHOUT ANY WARRANTY; without even the implied warranty of
// MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
// GNU General Public License for more details.
//
// You should have received a copy of the GNU General Public License
// along with this program.  If not, see <http://www.gnu.org/licenses/>.

using System.Xml.Serialization;

namespace KFS.Disks {
	/// <summary>
	/// Attributes of the master boot record.
	/// </summary>
	public class MasterBootRecordAttributes : Attributes, IDescribable {
		public MasterBootRecordAttributes() { }

		public MasterBootRecordAttributes(string description) {
			_description = description;
		}

		private string _description;
		[XmlIgnore]
		public override string TextDescription {
			get { return _description; }
		}
	}
}
